# DLL Function Patterns for Half-Life and friends

This repository contains a collection of function patterns or signatures of the game binaries of Half-Life and related games running the GoldSrc engine.

## How to add

The unmangled function names like `CGraph::InitGraph` are whitelisted in the JSON schema. To add a new function, you need to whitelist the function in the schema first. The pattern and symbol keys are similarly whitelisted. For example, if there is a new HL version like `HL-9000`, you would need to whitelist it in the schema as well.
