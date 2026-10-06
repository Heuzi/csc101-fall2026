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
        source ranges from row 910 to row 986. The old lookup against I:L
        returns credit hours, not a program code; see the lookup explanation
        in the instructor summary below.

        ### Reading Excel formulas and cell ranges

        A **cell reference** identifies one cell: `Q2` means column Q, row 2.
        A **range** identifies a group of cells. The colon (`:`) means
        **from the first reference through the second, including both ends**.
        It selects all cells between the endpoints, not just the endpoints.

        | Notation | Read it as | Cells included |
        | --- | --- | --- |
        | `M2:M5` | M2 through M5 | M2, M3, M4, M5: four cells in one column |
        | `R2:U2` | R2 through U2 | R2, S2, T2, U2: four cells in one row |
        | `Q2:U53` | Rectangle from Q2 to U53 | Columns Q, R, S, T, U and rows 2 through 53 |
        | `Q:U` | Columns Q through U | All cells in those five columns |
        | `2:986` | Rows 2 through 986 | All cells in those rows when used as an Excel reference |
        | `$M$2:$M$986` | Fixed range M2 through M986 | The same cells as M2:M986, with the endpoints locked for copying |

        In the instruction "fill R2:U2 down through row 53," select the four
        formula cells R2, S2, T2, U2 and copy them into the rows below through
        row 53. In labels such as `Q1: Program`, the colon is ordinary
        punctuation separating the cell address from its label.

        Other notation used in the formulas:

        - **`=` at the start:** tells Excel to calculate a formula. For example,
          `=T2/S2` divides the value in T2 by the value in S2. An `=` inside a
          condition, such as `M2=Q2`, tests whether two values are equal.
        - **Function names and parentheses:** a function is a named operation.
          Its inputs, called **arguments**, go inside parentheses, separated
          by commas: `FUNCTION(input1,input2)`. A function can use another
          function's result as an input; read those formulas from the inside out.
        - **`$` locks a reference for copying:** `$M$2` locks both column M and
          row 2. Without `$`, a reference adjusts when copied. For example,
          copying a formula from R2 to R3 changes its `Q2` input to `Q3`, but
          `$M$2:$M$986` stays the same. `$M2` locks only the column; `M$2`
          locks only the row.
        - **Double quotes:** mark literal text. `" "` means one space,
          `", "` means a comma followed by a space, and `""` means empty text.
        - **`&`:** joins text pieces. `"Thomas"&" "&"Ratkos"` produces
          `Thomas Ratkos`.

        Work on the same sheet without inserting or moving source columns.
        Use Excel for Microsoft 365, Excel 2021/2024, or Excel for the web for
        the list and sorting functions used below. Enter each list/sort formula
        once in its starting cell and leave its output area empty so results can **spill**
        into neighboring cells. A `#SPILL!` error usually means cells in that
        area are occupied.

        **What the totals measure:** the file has 985 rows but only 919 distinct
        section codes in B. Some section codes repeat with different rooms or
        instructors; some entire records repeat. The counting and summing
        exercises below operate on **source rows**, so label them accordingly.
        They do not produce deduplicated section totals or unique student
        counts. For example, CSC has 13 source rows but 11 distinct sections.

        ### 1. Full instructor name

        Put `Instructor name` in O1. In **O2**, enter:

        ```excel
        =TRIM(K2&" "&J2&" "&I2)
        ```

        **`TRIM(text)`** removes leading and trailing spaces and reduces
        repeated ordinary spaces between words to one space.

        Read this formula in two steps:

        1. `K2&" "&J2&" "&I2` joins the first name in K2, a space, the middle
           name in J2, another space, and the last name in I2.
        2. `TRIM(...)` cleans the joined text. If J2 is empty, the joining step
           creates two spaces between first and last name; TRIM reduces them
           to one.

        Fill O2 down through **O986**. O2 should show `Thomas Edward Ratkos`.
        Use this full-name column for instructor summaries: different people
        can share a last name.

        ### 2. Program summary (Q:U)

        | Header cell and label | First formula cell | Formula |
        | --- | --- | --- |
        | Q1: Program | Q2 | `=UNIQUE($M$2:$M$986)` |
        | R1: First location | R2 | `=INDEX($G$2:$G$986,MATCH(Q2,$M$2:$M$986,0))` |
        | S1: Course rows | S2 | `=COUNTIF($M$2:$M$986,Q2)` |
        | T1: Enrollment sum | T2 | `=SUMIF($M$2:$M$986,Q2,$E$2:$E$986)` |
        | U1: Avg per row | U2 | `=T2/S2` |

        **Q2: `UNIQUE(range)`** returns each distinct value in a range once.
        Here, `$M$2:$M$986` is the source list of program codes. Even though
        `ABA` appears on several rows, UNIQUE includes it only once in the
        result. Q2 spills **52 program codes** through Q53. UNIQUE removes
        repeats from its result; it does not delete source rows.

        **R2: `INDEX` and `MATCH` together.** The formula means:
        **"Find the program named in Q2 in column M, then return the location
        from column G on its first matching row."**

        ```excel
        =INDEX($G$2:$G$986,MATCH(Q2,$M$2:$M$986,0))
        ```

        Read the inner function first:

        1. **`MATCH(lookup_value,lookup_array,match_type)`** returns a value's
           **position within a range**, rather than returning that value.
           In `MATCH(Q2,$M$2:$M$986,0)`:
           - `Q2` contains the program to find, such as `ABA`.
           - `$M$2:$M$986` is the list to search.
           - `0` requests an **exact match**. If the program occurs more than
             once, MATCH returns the position of its first occurrence.
        2. **`INDEX(array,row_num)`**, used here with a single-column range,
           returns the value at a given position in that range. In this
           formula, `$G$2:$G$986` is the list of locations, and the result of
           MATCH supplies the position to retrieve.

        For example, Q2 is `ABA`, and the first `ABA` is in M2. That is position
        **1** in the range M2:M986, so MATCH returns **1**, not worksheet row
        number 2. The outer function becomes `INDEX($G$2:$G$986,1)`, which
        returns G2: **`COO`**. Both ranges start at row 2 and have the same
        length, so their positions refer to corresponding source rows.

        R2 must match **Q2**, not Q3. A program can use several locations, so
        this is only its **first matching location**, not its only building.
        Codes such as `ONLIN` and `TBA` are location labels in the source.

        **S2: `COUNTIF(range,criteria)`** counts cells in a range that meet
        one condition. `$M$2:$M$986` is the range to check, and `Q2` supplies
        the required program code. If Q2 is `ABA`, this counts four matching
        program cells, so the result is **4 course rows**. It does not add
        values or remove duplicate sections.

        **T2: `SUMIF(range,criteria,sum_range)`** adds values on rows that meet
        one condition. Its argument order differs from COUNTIF:

        - `$M$2:$M$986`: check these program cells.
        - `Q2`: keep rows whose program equals the code in Q2.
        - `$E$2:$E$986`: add enrollment values from those same rows.

        For ABA, the selected enrollment values are 23, 26, 16, and 11.
        Their sum is **76**. COUNTIF counts matching rows; SUMIF adds a
        numeric value from each matching row.

        **U2: `=T2/S2`** uses the division operator `/`, rather than a function.
        Enrollment sum divided by course-row count gives average enrollment
        per source row: for ABA, `76/4` is **19**.

        Fill **R2:U2 down through row 53**. Each copied formula uses the program
        code on its own summary row while keeping the source ranges fixed.

        Check the ABA row: **4 course rows, enrollment sum 76, average 19**.

        Copy the Q1:U1 headers to **W1:AA1**. In **W2**, enter:

        ```excel
        =SORT(Q2:U53,4,-1)
        ```

        **`SORT(array,sort_index,sort_order)`** returns a sorted copy of a range
        or list. It keeps each row's cells together and does not rearrange the
        original Q:U summary. In this formula:

        - `Q2:U53` is the entire five-column summary, excluding its header row.
        - `4` selects the fourth column **within that range**: Q is 1, R is 2,
          S is 3, and **T (enrollment sum) is 4**. This is not worksheet column D.
        - `-1` means descending: largest to smallest. `1` means ascending.

        W2 spills the sorted rows into W:AA. The first program should be BIO,
        with an enrollment sum of 1,157.

        ### 3. Sections with available seats (AD)

        Put `Section with seats` in AD1. In **AD2**, enter:

        ```excel
        =UNIQUE(FILTER($B$2:$B$986,$F$2:$F$986>0))
        ```

        **`FILTER(array,include,[if_empty])`** returns only the entries whose
        corresponding condition is TRUE. Square brackets in this syntax mean
        the `if_empty` argument is optional; do not type those brackets into
        the Excel formula. This example uses only the first two arguments.

        Read the formula from the inside out:

        1. `$F$2:$F$986>0` checks each available-seat value. `>` means "greater
           than," so 2 seats gives TRUE, while 0 or -1 gives FALSE.
        2. `FILTER($B$2:$B$986,$F$2:$F$986>0)` returns the section code in B
           wherever the value on the same row in F passed that test. The
           source and condition ranges have matching row positions.
        3. The outer `UNIQUE(...)` removes repeated section codes from that
           filtered list.

        This returns **662 section codes** through AD663. Zero seats means
        full; negative seats means over capacity. If no rows pass the test,
        FILTER without an `if_empty` argument returns `#CALC!`.

        ### 4. Instructor summary (AG:AJ)

        | Header cell and label | First formula cell | Formula |
        | --- | --- | --- |
        | AG1: Instructor name | AG2 | `=SORT(UNIQUE($O$2:$O$986))` |
        | AH1: First program | AH2 | `=INDEX($M$2:$M$986,MATCH(AG2,$O$2:$O$986,0))` |
        | AI1: Course rows | AI2 | `=COUNTIF($O$2:$O$986,AG2)` |
        | AJ1: Enrollment sum | AJ2 | `=SUMIF($O$2:$O$986,AG2,$E$2:$E$986)` |

        These functions work as introduced above, with instructor names as
        the grouping key:

        - **AG2:** UNIQUE gets distinct full names from O; the outer SORT has
          no extra arguments, so it sorts that single-column list in ascending
          alphabetical order by default.
        - **AH2:** MATCH finds the instructor named in AG2 in O; INDEX returns
          the program in M at that position.
        - **AI2:** COUNTIF counts source rows with that full name in O.
        - **AJ2:** SUMIF checks names in O, matches the name in AG2, and adds
          enrollment from E on matching rows.

        AG2 spills **261 distinct name labels** through AG262, including the
        placeholder `Berry Staff`. Fill **AH2:AJ2 down through row 262**.
        AH returns the program on the first matching instructor row. An
        instructor may teach in several programs; this is not a department
        affiliation.

        **`VLOOKUP(lookup_value,table_array,col_index_num,FALSE)`** is another
        lookup function. It searches the **first column** of its table range
        for an exact match (`FALSE`), then returns the value from a numbered
        column of that same table row. For the old table range `I:L`, I is
        column 1, J is 2, K is 3, and L is 4. Asking for column 4 therefore
        returns credit hours, not a program.

        A standard VLOOKUP retrieves columns to the right of its search
        column. Here we need to search full names in O and retrieve programs
        from M, which is to its left. INDEX/MATCH lets us choose the search
        and return ranges separately.

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

        **`TEXTJOIN(delimiter,ignore_empty,text1,...)`** combines text values
        into one cell, placing a chosen separator between them. Here:

        - `", "` is the separator: comma followed by a space.
        - `TRUE` tells TEXTJOIN to ignore empty text entries. `FALSE` would
          retain empty entries, which can create extra separators.
        - `SORT(UNIQUE(FILTER(...)))` supplies the list of location codes to join.

        For CSC, FILTER selects its location codes, UNIQUE reduces them to
        `MAC` and `HBL`, SORT puts `HBL` first, and TEXTJOIN produces
        **`HBL, MAC`** in one cell. Without TEXTJOIN, the list would spill into
        separate cells rather than become one comma-separated text value.

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

        **`ROWS(array)`** counts the number of rows in a range or returned
        list; it does not add the values in those rows. Here, FILTER keeps
        section codes for the program in Q2, UNIQUE keeps each section code
        once, and ROWS counts the resulting list. For CSC, FILTER finds 13
        source rows, UNIQUE leaves 11 section codes, and ROWS returns **11**.

        Change S1 to `Distinct sections`. This changes only the count:
        **do not divide the existing row-based enrollment sum by this new
        count**. Remove or revise U until enrollment is also summarized once
        per section. Simply removing duplicate entire rows is insufficient
        when the same section appears with different rooms or instructors.

        For another dataset, recheck the headers, last data row, and lengths
        of the program/instructor lists before reusing these ranges.

        Notation references: [Calculation and range operators](https://support.microsoft.com/en-us/excel/calculation-operators-and-precedence-in-excel),
        [Relative, absolute, and mixed references](https://support.microsoft.com/en-us/excel/switch-between-relative-absolute-and-mixed-references).

        Function references: [TRIM](https://support.microsoft.com/en-us/excel/functions/trim-function),
        [UNIQUE](https://support.microsoft.com/en-us/excel/functions/unique-function),
        [INDEX](https://support.microsoft.com/en-us/excel/functions/index-function),
        [MATCH](https://support.microsoft.com/en-us/excel/functions/match-function),
        [COUNTIF](https://support.microsoft.com/en-us/excel/get-started/use-the-countif-function-in-microsoft-excel),
        [SUMIF](https://support.microsoft.com/en-us/excel/functions/sumif-function),
        [FILTER](https://support.microsoft.com/en-us/excel/functions/filter-function),
        [SORT](https://support.microsoft.com/en-us/excel/functions/sort-function),
        [VLOOKUP](https://support.microsoft.com/en-us/excel/functions/vlookup-function),
        [TEXTJOIN](https://support.microsoft.com/en-us/excel/functions/textjoin-function),
        [ROWS](https://support.microsoft.com/en-us/excel/functions/rows-function).
        </details>


## Assignment

- [**Student grade book worksheet formulas [XGB]**](xgb/challenge_xgb.md)

- Complete LinkedIn Learning: [Linux Command Line (4, 5, conclusion)](https://www.linkedin.com/learning/learning-linux-command-line-14447912) [1hr 5m]

- Continue skill practice: [Typing](https://typing.com)


## References and Links
