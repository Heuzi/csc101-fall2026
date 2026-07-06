# Class 3 - Boolean logic; Satisfiability

## In-class

- Boolean logic
    - Practice [English -> Boolean Logic](https://www.cs.utexas.edu/~dnp/frege/practice-converting-between-english-and-boolean-logic.html)
    - [Truth table tool](https://web.stanford.edu/class/cs103/tools/truth-table-tool/)

- [Boolean satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)

- [Logic Puzzles and SAT Solvers: A match made in heaven](https://sabhijit.medium.com/logic-puzzles-and-sat-solvers-a-match-made-in-heaven-5e0a7a64c04b)
    - [Logic calculator](https://www.erpelstolz.at/gateway/formular-uk-zentral.html) - formula conversion
    - [SAT Solver](https://www.inf.ufpr.br/dpasqualin/d3-dpll/)

    <details>
        <summary>Demo</summary>

    ```
    45  <--- the number

    74  one correct, wrong place  =>  (s27 /\ -s14 /\ -s24 /\ -s17) \/ (s14 /\ -s17 /\ -s27 /\ -s24)
    93  no		      =>  -s19 ∧ -s29 ∧ -s13 ∧ -s23
    55  one correct place	      =>  (s15 ∧ -s25) v (-s15 ∧ s25)
    17  no		      =>  -s11 ∧ -s21 ∧ -s17 ∧ -s27

    https://www.erpelstolz.at/gateway/formular-uk-zentral.html
    (convert to CNF)

    #1: (s27 ∧ -s14 ∧ -s24 ∧ -s17) ∨ (s14 ∧ -s17 ∧ -s27 ∧ -s24)
            CNF: (S14 ∨ S27) ∧ (¬S27 ∨ ¬S14) ∧ ¬S24 ∧ ¬S17
    #2: -s19 ∧ -s29 ∧ -s13 ∧ -s23
    #3: (S25 ∨ S15) ∧ (¬S15 ∨ ¬S25)
    #4: -s11 ∧ -s21 ∧ -s17 ∧ -s27

    https://www.inf.ufpr.br/dpasqualin/d3-dpll/
    (remove the `s` prefixes)

    14   27
    -27 -14
    -24 -17
    -19 
    -29
    -13
    -23
    25 15
    -15 -25
    -11
    -21
    -17
    -27

    10 11 12 13 14 15 16 17 18 19
    20 21 22 23 24 25 26 27 28 29


    Solution: SATISFIABLE 14 25 -19 -29 -13 -23 -11 -21 -17 -27 -15
    ```

    </details>


## Assignments

- LinkedIn Learning: [Linux Command Line (intro, part 1+2+3)](https://www.linkedin.com/learning/learning-linux-command-line-14447912) [1hr 49m]

- [WTQ] [Write the Question - Linux/CLI](linux-ques.md)

- [**[SAT] Boolean Satisfiability Challenge**](./sat.md)

- Continue skill practice: [Typing](https://typing.com)




## References and Links

- [Boolean Logic](https://www.cs.utexas.edu/~dnp/frege/chapter-2.html) chapter of *Reasoning: An Introduction to Logic, Sets, and Functions*

- [Boolean Game](https://boolean.method.ac/) - random fun - image editing tools
