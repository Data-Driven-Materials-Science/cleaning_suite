# Cleaning Suite Developer Notes
By Ashley Schuliger and Christopher Vieira

## Formatting and Coding Practices
Some general formatting and coding practices should be followed when adding to this project. This ensures that 
the code is readable, usable, and modifiable. The purpose of this project is to create a very modular suite which
other developers can use in order to clean their data. A list below represents practices to follow during your
development of this project.
- Simple Coding
  - Operations should only be one line
    - You should not go over the IDE character limit for a line (shown by the grey line on the side)
  - You should not have nested / cascading function calls
    - Something like array[lambda x: func_call(x=variable):other_func_call(y=another_func(z=10))]
      - This should be 4 lines at least. Every func call should be set to a variable first and then
      the array operation should take place.
  - Variables should be properly named in a clear and concise way. They should not be long but it should be
  obvious what the variable represents without a comment. Below are some examples of variable names.
    - Good examples:
      - excel_df
      - samples_ids_list
      - i as an iterator (ideally an integer value)
    - Bad Examples:
      - probability_density_function_raw_values_before_processing
      - x
      - i as anything but an iterator
- Class Structure
  - Classes should typically be structured as a collection of helper methods. Object Oriented classes should not
   be used in this project.
  - Class A can use methods from Class B, but Class B can not use methods from Class A. We do not want
  cyclical calls between classes or development becomes a nightmare.
    - If you drew out all of the connections between classes then it should look like a tree, not a graph
  - Every method should have one function and ONLY one function. 
    - Think of the task where you are making a method which removes outliers but you need to transform the data first. 
    Make a method to transform the data beforehand and call this method at the start of the method you are 
    implementing. You'll want to do this for the following reasons:
- Package Structure
  - A package represents a collection of classes with the same general theme such as handling outliers, null, etc.
  The package structure can be minimally modified but you should never delete existing packages. It should only be 
  modified in the following situations:
    - If there are a group of classes (5+) which are more specific than the parent folder then they should
    be placed into their own package. An example of this could be if 5 classes each handled removing outliers
    from a data set. They may be placed in a sub folder called outlier_removers in the outlier_handlers folder.
    - If any classes are made which do not fit anywhere in the package structure then a new package should be
    made. For example, if you started implementing something which handles specifically stress strain curves
    and the data associated with them then it should be a separate folder in the helper_functions holder.
- Other Coding Practices
  - Never copy code from another location in the project. If you need to use the same code in another function,
  the correct way to handle this would be to move the copied code into a helper method that both your new code 
  and the original section which used it can call.
  - Check Github issues before making your own. Make sure that the issue you are creating has not been solved
  and that it isn't being worked on by someone else.
  - If you and another developer are working on the project at the same time, check in with them to see 
  what sections they are working on. Ensuring that you aren't editing the same files lessens the chance of
  merge conflicts.

## Commenting
Comments must be done in a certain format. Every method must have doc strings in the format
used by Pycharm's auto formatting. An example of this is below.

    """

    :param clustering_method: The clustering method we are using, see StringDefinitionsHelper for options
    :param clustering_details: The details associated with the clustering method we are using, see
        StringDefinitionsHelper
    :param file_name: The name of the file we are reading in relative to the folder of the executable
    :param file_format: The format of the file we are reading in, see StringDefinitionsHelper for options
    :param clustered_column: The name of the type of column we are clustering, default value of Hardness

    :return: Nothing at the moment

    Reads in all of the data and performs the necessary clustering. It performs the following steps: Reading in the
    data, preprocessing the data, clustering the data, an then analyzing the data. The the respective helper classes
    for more details as to how the processes work. 

    """
    
Notice that every parameter has :param in front of their names and then a brief description as to what it does.
Along with this, notice that there is an indent should a description take more than one line.
The return statement then has :return: in front of it along with a brief description.
Another new line is added and then the general description of the function itself is given.

This formatting not only is good practice, but it is necessary for the auto-documentation software to 
function properly. If you do not follow then then you will break it.

## Addition Policies
When adding to the project, you must branch off of main. Ideally, this project will be
used in the functionality of several other projects so it is critical you follow
proper Github practices when adding content. This involves the following steps:

- Creating an issue describe what needs to be fixed or what the project is lacking
- Branching off of the current development branch
- Completing the necessary work to add your content or fix an issue
- Submit a pull request and reach out to another developer to have them approve the pull request
- Merging your branch with the current development branch and then deleting your branch

Any additions to the project should be given proper review to prevent issues which can 
propagate to other projects.

You do not need to follow these strictly for testing but do need to for the final product.
