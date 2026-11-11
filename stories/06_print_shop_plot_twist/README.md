# The Print-Shop Plot Twist

Nakato’s group report is ready. The colourful cover is beautiful; the printing budget is considerably less beautiful.

This story includes all the OOP concepts from Weeks 1 to 6. The numbers are made up for learning.

## Group assignment

The combined assignment is due at the end of **Wednesday, 21 October 2026, Uganda time**. Keep your [foundation work](EXTENSIONS.md), then choose three [later-topic extensions](ADVANCED_EXTENSIONS.md). Each member contributes foundation work and new code or meaningful automated tests through reviewed PRs. The [common assignment](../../GROUP_ASSIGNMENT.md) explains the workflow and what to submit.

## Run this story

If you have not downloaded the files yet, follow [Start here](../../START_HERE.md).

1. Open the repository folder in VS Code.
2. Open `stories/06_print_shop_plot_twist/story.py`.
3. Choose **Run Python File in Terminal**, or use the command below.

From a terminal in the main repository folder:

**Windows:**

```sh
py -3 stories/06_print_shop_plot_twist/story.py
```

**macOS or Linux:**

```sh
python3 stories/06_print_shop_plot_twist/story.py
```

The whole story prints without asking you to type anything. Open [expected_output.txt](expected_output.txt) to see the output of the unchanged program.

## Read the five acts

**Act 1 — the rule keeper.** `PrintCredit` keeps the changing resource. Its constructor sets a valid starting value. Its property getter reads that value. Its setter refuses a negative value. Its action method refuses a request that does not fit.

**Act 2 — the family.** `OutputOption` is an abstract class. It says that every concrete member of the family must provide `quote(pages)`. `BlackAndWhite` and `Colour` provide different versions. `super().__init__()` reuses the parent's setup.

**Act 3 — the special choices.** `StudentPrint` extends `BlackAndWhite`. `FriendlyStudentPrint` adds the description from `FriendlyMixin` using multiple inheritance. `PDFSubmission` is not in the same family but provides the methods the program needs.

**Act 4 — the coordinator.** `ReportSession` creates and owns a `PrintCredit`. It receives a choice object, asks it for its behaviour and lets the resource object check the request. Successful actions go into its own history list. `completed_outputs` reads the length of that list and has no setter.

**Act 5 — the complete story.** `main()` creates the objects and runs their actions. Two coordinator objects show that one person's resource and history are separate from another's.

## One request, step by step

`nakato.produce(options[2], 4)` requests a quote. `StudentPrint.quote()` asks BlackAndWhite for 800 and subtracts the sponsored first page’s 200. The PrintCredit pays 600, then the output is recorded. The same ReportSession later swaps to a PDF collaborator without changing its pricing code.

## The ending, with the numbers explained

| Event | Resource after the attempt | Completed count |
|---|---|---|
| Colour report | Refused: 4 × 1,000 = 4,000 > 1,000 | 0 |
| Student printing | 1,000 - (4 × 200 - 200) = 400 | 1 |
| PDF archive | 400 - 0 = 400 | 2 |
| Okello prints black-and-white | 800 - (4 × 200) = 0 | 1 (Okello only) |

A refused request changes neither the guarded resource nor the completed-action count.

## How the classes connect

```mermaid
classDiagram
    OutputOption <|-- BlackAndWhite
    OutputOption <|-- Colour
    BlackAndWhite <|-- StudentPrint
    StudentPrint <|-- FriendlyStudentPrint
    FriendlyMixin <|-- FriendlyStudentPrint
    ReportSession *-- PrintCredit : owns
    ReportSession --> OutputOption : uses
    ReportSession --> PDFSubmission : uses same methods
```

`BlackAndWhite` **is a kind of** `OutputOption`. That is inheritance.

`ReportSession` **has its own** `PrintCredit`. That is composition. It is not a kind of that resource.

Choice objects are created outside the coordinator. Passing them in is association. Keeping references to those independent objects is aggregation.

## Where each concept appears

| Concept | In this story |
|---|---|
| Classes, objects, attributes and methods | The class definitions and the objects created in `main()` |
| Constructors and `self` | Each `__init__`; `self` means the object receiving that call |
| Class and instance attributes | The shared fact on `OutputOption` and the separate values kept by each object |
| Encapsulation | `PrintCredit` stores a resource and checks its changes |
| Public, `_` and `__` names | Public methods, the internal history list and the name-mangled resource value |
| Getter, validating setter and read-only property | `balance` on the resource; `completed_outputs` on the coordinator |
| Single and hierarchical inheritance | `BlackAndWhite` and `Colour` inherit `OutputOption` |
| Multilevel inheritance | `OutputOption → BlackAndWhite → StudentPrint` |
| Multiple and hybrid inheritance | `FriendlyStudentPrint` combines the mixin with that family |
| Overriding and `super()` | The specialised calculation and the added description |
| Polymorphism | The mixed-object loop in `compare_outputs()` |
| Duck typing | `PDFSubmission` works without inheriting `OutputOption` |
| MRO | The ordered class list printed near the ending |
| Abstraction and abstract classes | `OutputOption` requires `quote(pages)`; the caller uses it without reproducing its calculation |
| Composition and object collaboration | `ReportSession` owns its resource and works with choice objects |
| UML relationships | The class diagram above |
| Python refresher | Functions, parameters, defaults, returned values, lists, loops, conditions and arithmetic |

Read [OOP in plain English](../../OOP_IN_PLAIN_ENGLISH.md) for a simple explanation of the terms.
