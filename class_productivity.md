# Productivity: Excel, Kanban, VS Code

## In-class

- [Kanban](https://en.wikipedia.org/wiki/Kanban_(development))
    - [Portable Kanban](https://marketplace.visualstudio.com/items?itemName=harehare.portable-kanban) - VS code extension

- [Spreadsheets](https://e115.engr.ncsu.edu/spreadsheets/)
    - [course-data-fall-2025.xlsx](./class05-course-data-fall-2025.xlsx)
    
    - <details>
        <summary>(notes for self)</summary>

        ### Workbook layout

        These formulas match **Sheet1** in the linked Fall 2025 workbook. Row 1
        contains headers; **rows 2:986 contain 985 data records**. Rows 987:1051
        are empty despite being included in the worksheet's formatted area.

        | Column | Header | Meaning |
        | --- | --- | --- |
        | A | `year_term` | Term code |
        | B | `crs_cde` | Course code including section, e.g. `ABA222 A` |
        | C | `crs_title` | Course title |
        | D | `capacity` | Capacity |
        | E | `enrollment` | Enrollment on this record |
        | F | `seats_available` | Available seats; positive means open |
        | G | `bldg_cde` | Building/location code |
        | H | `room_cde` | Room code |
        | I | `last` | Instructor last name |
        | J | `middle` | Instructor middle name |
        | K | `first` | Instructor first name |
        | L | `credit_hrs` | Credit hours |
        | M | `crs_comp1` | Program/subject prefix, e.g. `ABA`, `CSC` |
        | N | `crs_comp2` | Course number, e.g. `222`, `101` |

        **Changes from the old notes:** use M for program codes, not L. Add the
        full name in O, because N already contains course numbers. Extend the
        source ranges from row 910 to row 986. The old `VLOOKUP` against I:L
        returns credit hours, not a program code.

        Work on the same sheet without inserting or moving source columns.
        Use Excel for Microsoft 365, Excel 2021/2024, or Excel for the web for
        `UNIQUE`, `FILTER`, and `SORT`. Enter each list/sort formula once in its
        starting cell and leave its output area empty so results can **spill**
        into neighboring cells. A `#SPILL!` error usually means cells in that
        area are occupied. The `$` signs keep source ranges fixed when filling
        formulas down.

        **What the totals measure:** the file has 985 rows but only 919 distinct
        section codes in B. Some section codes repeat with different rooms or
        instructors; some entire records repeat. The `COUNTIF` and `SUMIF`
        exercises below count/sum **source rows**, so label them accordingly.
        They do not produce deduplicated section totals or unique student
        counts. For example, CSC has 13 source rows but 11 distinct sections.

        ### 1. Full instructor name

        Put `Instructor name` in O1. In **O2**, enter:

        ```excel
        =TRIM(K2&" "&J2&" "&I2)
        ```

        Fill O2 down through **O986**. `&` joins the name parts; `TRIM` removes
        extra spaces when a middle name is missing. O2 should show
        `Thomas Edward Ratkos`. Use this full-name column for instructor
        summaries: different people can share a last name.

        ### 2. Program summary (Q:U)

        | Header cell and label | First formula cell | Formula |
        | --- | --- | --- |
        | Q1: Program | Q2 | `=UNIQUE($M$2:$M$986)` |
        | R1: First location | R2 | `=INDEX($G$2:$G$986,MATCH(Q2,$M$2:$M$986,0))` |
        | S1: Course rows | S2 | `=COUNTIF($M$2:$M$986,Q2)` |
        | T1: Enrollment sum | T2 | `=SUMIF($M$2:$M$986,Q2,$E$2:$E$986)` |
        | U1: Avg per row | U2 | `=T2/S2` |

        Q2 spills **52 program codes** through Q53. Fill **R2:U2 down through
        row 53**. R2 must match **Q2**, not Q3. `MATCH(...,0)` finds the first
        exact program match, and `INDEX` returns the location on that row.
        A program can use several locations, so this is only its **first
        matching location**, not its only building. Codes such as `ONLIN` and
        `TBA` are location labels in the source.

        Check the ABA row: **4 course rows, enrollment sum 76, average 19**.

        Copy the Q1:U1 headers to **W1:AA1**. In **W2**, enter:

        ```excel
        =SORT(Q2:U53,4,-1)
        ```

        This sorts the complete program summary by enrollment, largest first.
        `4` means the fourth column **within Q:U** (T), and `-1` means descending.
        The first program should be BIO, with an enrollment sum of 1,157.

        ### 3. Sections with available seats (AD)

        Put `Section with seats` in AD1. In **AD2**, enter:

        ```excel
        =UNIQUE(FILTER($B$2:$B$986,$F$2:$F$986>0))
        ```

        `FILTER` keeps rows with positive available seats, then `UNIQUE`
        removes repeated section codes. This returns **662 section codes**
        through AD663. Zero seats means full; negative seats means over capacity.

        ### 4. Instructor summary (AG:AJ)

        | Header cell and label | First formula cell | Formula |
        | --- | --- | --- |
        | AG1: Instructor name | AG2 | `=SORT(UNIQUE($O$2:$O$986))` |
        | AH1: First program | AH2 | `=INDEX($M$2:$M$986,MATCH(AG2,$O$2:$O$986,0))` |
        | AI1: Course rows | AI2 | `=COUNTIF($O$2:$O$986,AG2)` |
        | AJ1: Enrollment sum | AJ2 | `=SUMIF($O$2:$O$986,AG2,$E$2:$E$986)` |

        AG2 spills **261 distinct name labels** through AG262, including the
        placeholder `Berry Staff`. Fill **AH2:AJ2 down through row 262**.
        AH returns the program on the first matching instructor row. An
        instructor may teach in several programs; this is not a department
        affiliation. `INDEX/MATCH` also lets us look left from O (full name)
        to M (program), which a standard `VLOOKUP` cannot do.

        Copy the AG1:AJ1 headers to **AL1:AO1**. In **AL2**, enter:

        ```excel
        =SORT(AG2:AJ262,4,-1)
        ```

        Enrollment is the **fourth** column of AG:AJ (AJ). The old sort index
        `3` sorted by course-row count instead. The old ending row 216 would
        also omit some instructors.

        ### Optional: show all matching locations/programs

        To show every distinct location for each program, change R1 to
        `Locations` and replace R2 with this formula, then fill down:

        ```excel
        =TEXTJOIN(", ",TRUE,SORT(UNIQUE(FILTER($G$2:$G$986,$M$2:$M$986=Q2))))
        ```

        For CSC, the result should be `HBL, MAC`.

        To show every program an instructor teaches in, change AH1 to
        `Programs` and replace AH2 with this formula, then fill down:

        ```excel
        =TEXTJOIN(", ",TRUE,SORT(UNIQUE(FILTER($M$2:$M$986,$O$2:$O$986=AG2))))
        ```

        Read these from the inside out: `FILTER` selects matching rows,
        `UNIQUE` removes repeats, `SORT` orders the codes, and `TEXTJOIN`
        combines them in one cell.

        To count distinct sections for a program instead of source rows,
        use this in S2 and fill down:

        ```excel
        =ROWS(UNIQUE(FILTER($B$2:$B$986,$M$2:$M$986=Q2)))
        ```

        Change S1 to `Distinct sections`. This changes only the count:
        **do not divide the existing row-based enrollment sum by this new
        count**. Remove or revise U until enrollment is also summarized once
        per section. Simply removing duplicate entire rows is insufficient
        when the same section appears with different rooms or instructors.

        For another dataset, recheck the headers, last data row, and lengths
        of the program/instructor lists before reusing these ranges.

        Function references: [UNIQUE](https://support.microsoft.com/en-us/excel/functions/unique-function),
        [FILTER](https://support.microsoft.com/en-us/excel/functions/filter-function),
        [SORT](https://support.microsoft.com/en-us/excel/functions/sort-function),
        [TEXTJOIN](https://support.microsoft.com/en-us/excel/functions/textjoin-function).
        </details>


## Assignment

- [**Student grade book worksheet formulas [XGB]**](xgb/challenge_xgb.md)

- Complete LinkedIn Learning: [Linux Command Line (4, 5, conclusion)](https://www.linkedin.com/learning/learning-linux-command-line-14447912) [1hr 5m]

- Continue skill practice: [Typing](https://typing.com)


## References and Links
