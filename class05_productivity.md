# Class 5 - Productivity: Excel, Kanban, VS Code

## In-class

- [Kanban](https://en.wikipedia.org/wiki/Kanban_(development))
    - [Portable Kanban](https://marketplace.visualstudio.com/items?itemName=harehare.portable-kanban) - VS code extension

- [Spreadsheets](https://e115.engr.ncsu.edu/spreadsheets/)
    - [course-data-fall-2025.xlsx](./class05-course-data-fall-2025.xlsx)
    
    - <details>
        <summary>(notes for self)</summary>

        ```
        Add full professor name in column N   = .. & ..

        Unique programs: =UNIQUE(L2:L910)           <-- in column Q
        Bldg associated with program: =INDEX(G:G, MATCH(Q3,L:L,0))
        Total course/prog:  =COUNTIF(L:L,Q2)
        Total enrollment:   =SUMIF(L:L,Q2,E:E)
        Avg enrollment:    =T2/S2

        Sorted by enrollment (W)  =SORT(Q2:U216,4,-1)

        Open courses (AD)   =UNIQUE(FILTER(B2:B910, F2:F910>0))

        Instructor (unique) (AG)   =SORT(UNIQUE(I2:I910))
        Program                    =VLOOKUP(AG2,$I$2:$L$910,4,FALSE)
        Total courses taught      =COUNTIF(I:I,AG2)
        Total enrollment          =SUMIF(I:I,AG2,E:E)

        Instr/Sorted by enrollment (AL)   =SORT(AG2:AJ216,3,-1)
        ```
    </details>


## Assignment

- [**Student grade book worksheet formulas [XGB]**](xgb/xgb.md)

- Complete LinkedIn Learning: [Linux Command Line (4, 5, conclusion)](https://www.linkedin.com/learning/learning-linux-command-line-14447912) [1hr 5m]

- [Advent of Cyber 2024](https://tryhackme.com/room/adventofcyber2024)

- Continue skill practice: [Typing](https://typing.com)


## References and Links
