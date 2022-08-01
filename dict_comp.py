# Core Python 3: Dictionary Comprehensions
# Course: https://app.pluralsight.com/library/courses/getting-started-python-core/table-of-contents

country_to_capital = {'United Kingdom': 'London',
                      'Sweden': 'Stockholm',
                      'Norway': 'Oslo',
                      'Bulgaria': 'Sofia',
                      'Libya': 'Tripoli',
                      'Denmark': 'Copenhagen',
                      'Spain': 'Madrid',
                      'Taiwan': 'Taipei',
                      }

# Dictionary comprehension from existing dictionary
capital_to_country = {capital: country
                      for country, capital
                      in country_to_capital.items()}
print(capital_to_country)

# Dictionary comprehension from list
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
letterAndString = {s[0]: s for s in numbers}
print(letterAndString)
