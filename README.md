# slashcolonlang

#### The file extension ".sc" stands for ".slashcolon".

SlashColon started out as an idea looking at transistors. Transistors are either 1 or 0, on or off. Then my project slowly started moving towards a stack-based "project" if you will.

The correct usage for the main.py file is:

**python3 <main.py> <grabfrom.sc> [--options]**

- /
  - Add 1 (one) integer to the current stack value
- ;
  - Subtract 1 (one) integer from the current stack value
- ]
  - Add 10 (ten) integers to the current stack value
- *
  - Multiply the current stack value by 2 (two)
- -
  - Break the current stack and save it into script memory, and also create and move into a new stack position

After the script has executed, it will print out all the stack values in a list. If you used the optional argument ``--ascii`` then all values will be converted to their ascii partners.

Example 1:
``py main.py grabfrom.sc``
```
]***]]/////
-
/////
-
;;;;;
```
```
Output:
[105, 5, -5]
```

Example 2:
``py main.py grabfrom.sc --ascii``
```
]]]]]]]//
-
]]]]]]]]]]/
-
]]]]]]]]]]////////
-
]]]]]]]]]]////////
-
]]]]]]]]]]]/
-
]]]]////
-
]]]//
-
]]]]]]]]]]]/////////
-
]]]]]]]]]]]/
-
]]]]]]]]]]]////
-
]]]]]]]]]]////////
-
]]]]]]]]]]
-
]]]///
-
```
```
Output:
Hello, world!
END
```