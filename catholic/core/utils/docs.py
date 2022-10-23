def paragraph_help_text():
    return """
              Query using Paragraph Number. This takes in a variety of inputs.

              Possible Input Examples:

              --p 101 - Returns Paragraph with ID 101.

              --p 101-105 - Returns the paragraphs within the given range.

              --p 101,102 - Returns the paragraphs in the given list.

              --p 101,103-105,110,111 - This is a combination of the above possibilities
              separated by commas.

              Note that the value part of the option does not have spaces. Eg: --p 101,103-105,110,111.
              If you wish to add space in the value, you can enclose the value within double quotes like so:
              --p "101, 103 - 105, 110, 111".

              """


def search_help_text():
    return """
              Search this resource for the given string. Currently the search functionality is very limited.
              catholic-cli looks up for an exact match. More NLP based search features are on the way!
              
              Examples:
              
              --search "the eucharist"
              
              --s "the eucharist" 
           """
