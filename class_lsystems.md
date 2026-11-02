# L-systems; Formal grammars

## Grammar basics

- **Grammar:** a set of rules for building strings of symbols.
- **Symbol and string:** a symbol is one item, such as `A` or `B`. A string is an ordered sequence of symbols, such as `AAB`.
- **Start symbol (axiom):** the symbol or string we begin with. `Axiom: S` means start with `S`.
- **Replacement rule (production):** a rule tells us what a symbol can become. `T = AT` means we may replace a `T` with `AT`. Here, `=` means "can be replaced by," rather than mathematical equality.
- **Terminal and nonterminal:** a terminal stays in the finished string; a nonterminal is a placeholder we replace while building it. In the examples that start with `S`, `A` and `B` are terminals, while `S` and `T` are nonterminals.
- **Empty string (`ε`):** a string with no symbols. A blank right-hand side, such as `T =`, means replace `T` with nothing.
- **Alternative rules:** commas separate choices. `T = AT,BT,` means replace `T` with `AT`, `BT`, or the empty string. Choose one alternative each time you replace a `T`.

## In-class

- Grammars

    ```
    // Lindenmayer's original L-system for modelling the growth of algae.
    Axiom: A
    A = AB
    B = A

    // contains a single B
    Axiom: S
    S = TBT
    T = AT
    T = TA
    T = 

    // starts w/ a ends w/ b
    Axiom: S
    S=ATB
    T=AT,BT,

    // equal #s of a's & b's
    Axiom: S
    S = ASB,BSA,SS, 
    ```

    - Parsing...

- Lindenmayer systems (l-systems)

    ```
    F = draw forward
    + = turn right by <angle>
    - = turn left by <angle>
    [ = push location (save)
    ] = pop location (return to last saved/undo)
    ```

    example: `A=F+F++F+F-F--F-F`
  
    - Try at: https://piratefsh.github.io/p5js-art/public/lsystems/



## Assignment

-  [Grammars & L-system design [LSY]](lsy/challenge_lsy.md)


## Resources

- https://en.wikipedia.org/wiki/L-system
- https://paulbourke.net/fractals/lsys/ (examples)
- https://algorithmicbotany.org/
- https://web.stanford.edu/class/archive/cs/cs103/cs103.1156/tools/cfg/

- https://en.wikipedia.org/wiki/Context-free_grammar#Examples
- https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form#Example

<!-- https://www.russellgordon.ca/cemc/2017/lindenmayer-systems/ -->
