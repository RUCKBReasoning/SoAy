# Quick Construction Guide

> by WangYC

This is a guide that explains how to rapidly construct corresponding datasets and applications based on an existing API system.

## 0. Config Filling

Go to config directory and make your own config file according to the examples in the same directory.

```shell
cd SoAy/config
vim ${DOMAIN_NAME}_function_config.jsonl
```

## 1. API Graph Construction & Combination Generation

```shell
cd SoAy/SolutionLibrary_toolkit
```

Create a directory to save your Graph and Combination File.

```shell
mkdir ${DOMAIN_NAME}
```

Edit the variant `domain` and`start_node_list` in `solution_construction.py` line 121 and 130.

```python
		#Instantiate
    domain = 'AMiner'
    # domain = 'OpenLibrary'
    # domain = 'Crossref'
    toolkit = solution_toolkit(domain = domain)

    #Configs
    config_file_path = '../config/{}_function_config.jsonl'.format(domain)
    info_dict_list = toolkit.collectInformation(config_file_path)
    start_node_list = ['searchPerson', 'searchPublication'] #AM
    # start_node_list = ["searchBook", "searchAuthor", "searchSubject"] #OL
    # start_node_list = ["searchPublisherBySubject", "searchWorksByTitle", "searchWorksByAuthor"] #CR
```

Note that here we set the `road sampling hop maximum = 3` to ensure the solution not too complecated. (line 10)

Run the combination generation program

```shell
python solution_construction.py
```

All possible solutions will be listed in your terminal.

An API Graph in the format of html is constructed in the target directory  `SolutionLibrary_toolkit/results/${DOMAIN_NAME}/`

Also, a Combination file which may lead you build your dataset or examples in prompt is generated in the same dir.

## 2. Prompt Design

```shell
cd SoAy/prompts_toolkit
```

### 2.A General Prompt Crafting (for quick construction)

Craft your prompt according to the AMiner example `SoAy/SolutionLibrary_toolkit/prompt_txt/`

The structure is  :

* API Description

  ```
  Here are some tool functions you can use. Each function returns a dict or a list of dict.
  ------
  API_1
  ---
  API_2
  ---
  ...
  ---
  API_n
  ------
  ```

* Examples

  ```
  The following example shows you how to use these tools in practical tasks. You are given a query. Break the query down into a combination of the python execution processes in order to solve it.
  ---
  Query_1
  Solution_1
  --
  Code_1
  ---
  Query_2
  Solution_2
  --
  Code_2
  ---
  Query_3
  Solution_3
  --
  Code_3
  ```

* New Query

  ```
  ---
  New_Query
  ```

### 2.B Detailed Prompt Crafting (for dataset construction)

To build a trianing set or testing set, more precise data is needed.

Firstly build template questions using QG_prompt `template_questions_prompt.txt`

Fill the real collected entities into the temlate to get the **[Query]**

Then generate relevant **[Code]** using Code_prompt `codes_generation_prompt.txt`

Run the generated codes to reach the **[Answer]** to the **[Query]**

Now, a piece of dataset {Query, Code, Answer} is constructed.

To build a more precise pipeline using codes & sulution retrieval, use the method above to construct a detailed prompt, e.g. `Detailed_prompt_AMiner`.



