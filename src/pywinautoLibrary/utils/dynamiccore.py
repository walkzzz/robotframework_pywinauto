# Copyright 2023-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class DynamicCore:
    """Simplified implementation of DynamicCore for keyword composition.
    
    This class is used to dynamically compose keywords from multiple libraries.
    """
    
    def __init__(self, libraries):
        """Initialize DynamicCore with a list of libraries.
        
        :param libraries: List of library instances containing keywords.
        :type libraries: list
        """
        self._keywords = {}
        self._library_instances = libraries
        self._register_keywords()
    
    def _register_keywords(self):
        """Register keywords from all libraries.
        """
        for library in self._library_instances:
            # Get all public attributes from the library instance
            for name in dir(library):
                if name.startswith('_'):
                    continue
                
                # Skip properties to avoid triggering them during registration
                try:
                    # Check if it's a property by accessing __dict__ chain
                    is_property = False
                    for base in library.__class__.__mro__:
                        if name in base.__dict__ and isinstance(base.__dict__[name], property):
                            is_property = True
                            break
                    if is_property:
                        continue
                    
                    # Get the attribute and check if it's callable
                    attr = getattr(library, name)
                    if callable(attr):
                        # Register the keyword if not already registered
                        if name not in self._keywords:
                            self._keywords[name] = attr
                except Exception:
                    # Skip any attributes that cause errors when accessed
                    continue
    
    def __getattr__(self, name):
        """Get attribute by name, checking keywords if not found in instance.
        
        This method allows direct calling of registered keywords as instance methods.
        
        :param name: Name of the attribute or keyword to get.
        :type name: str
        :return: The attribute or keyword function.
        :rtype: Any
        :raises AttributeError: If the attribute or keyword is not found.
        """
        # Try to get the keyword from the registry
        if name in self._keywords:
            return self._keywords[name]
        # If not found, raise AttributeError as usual
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def run_keyword(self, name, args, kwargs):
        """Run a keyword with the given name and arguments.
        
        :param name: Name of the keyword to run.
        :type name: str
        :param args: Positional arguments for the keyword.
        :type args: tuple
        :param kwargs: Keyword arguments for the keyword.
        :type kwargs: dict
        :return: The result of the keyword execution.
        :rtype: Any
        :raises AttributeError: If the keyword is not found.
        """
        # Try exact match first
        if name in self._keywords:
            return self._keywords[name](*args, **kwargs)
        
        # Try case-insensitive match
        for keyword_name, keyword in self._keywords.items():
            if keyword_name.lower() == name.lower():
                return keyword(*args, **kwargs)
        
        raise AttributeError(f"Keyword '{name}' not found.")
    
    def get_keyword_names(self):
        """Get the names of all available keywords.
        
        :return: List of keyword names.
        :rtype: list
        """
        return list(self._keywords.keys())
