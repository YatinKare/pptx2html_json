\n--- Page 2719 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
depthByBranch (Diagram Build Type Enum ( Depth By Depth By Branch
Branch ))
depthByNode (Diagram Build Type Enum ( Depth By Depth By Node
Node ))
down (Diagram Build Type Enum ( Down )) Down
inByRing (Diagram Build Type Enum ( In-By-Ring )) In-By-Ring
outByRing (Diagram Build Type Enum ( Out-By-Ring )) Out-By-Ring
up (Diagram Build Type Enum ( Up )) Up
whole (Diagram Build Type Enum ( Whole )) Whole
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLDiagramBuildType) is located
in §A.3. end note]
19.7.34 ST_TLNextActionType (Next Action Type)
This simple type specifies what to do when going forward in a sequence. When the value is "seek," it seeks the
current child element to its natural end time before advancing to the next element.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
none (Next Action Type Enum ( None )) None
seek (Next Action Type Enum ( Seek )) Seek
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLNextActionType) is located in
§A.3. end note]
19.7.35 ST_TLOleChartBuildType (Embedded Chart Build Type)
This simple type describes how to build an embedded Chart.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allAtOnce (Chart Build Type Enum ( All At Once )) All At Once
category (Chart Build Type Enum ( Category )) By Category
categoryEl (Chart Build Type Enum ( Category Element By Category Element
))
©ISO/IEC 2016 – All rights reserved 2709\n\n--- Page 2720 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
series (Chart Build Type Enum ( Series )) By Series
seriesEl (Chart Build Type Enum ( Series Element )) By Series Element
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLOleChartBuildType) is located
in §A.3. end note]
19.7.36 ST_TLParaBuildType (Paragraph Build Type)
This simple type describes how to build a paragraph.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allAtOnce (All At Once) Specifies to animate all paragraphs at once.
cust (Custom) Specifies the build has custom user settings.
p (Paragraph) Specifies to animate paragraphs grouped by bullet
level.
whole (Whole) Specifies to animate the entire body of text as one
block.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLParaBuildType) is located in
§A.3. end note]
19.7.37 ST_TLPreviousActionType (Previous Action Type)
This simple type specifies what to do when going backwards in a sequence. When the value is "skipTimed," the
sequence continues to go backwards until it reaches a sequence element that was defined to being only on a
"next" event.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
none (Previous Action Type Enum ( None )) None
skipTimed (Previous Action Type Enum ( Skip Timed )) Skip Timed
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLPreviousActionType) is
located in §A.3. end note]
2710 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2721 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.38 ST_TLTime (Time)
This simple type specifies time after which to automatically advance the build to the next step. An amount of
time, in milliseconds.
This simple type is a union of the following types:
 The ST_TLTimeIndefinite simple type (§19.7.40).
 The W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTime) is located in §A.3. end
note]
19.7.39 ST_TLTimeAnimateValueTime (Animation Time)
This simple type specifies a percentage within the time span of the element. A value of indefinite means the
attribute should be ignored.
This simple type is a union of the following types:
 The ST_PositiveFixedPercentage simple type (§20.1.10.45).
 The ST_TLTimeIndefinite simple type (§19.7.40).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeAnimateValueTime) is
located in §A.3. end note]
19.7.40 ST_TLTimeIndefinite (Indefinite Time Declaration)
This simple type specifies a value that designates an "indefinite" amount time -- typically means this property is
subordinate to other, defined properties.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
indefinite (Indefinite Type Enum) Specifies Indefinite Time
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeIndefinite) is located in
§A.3. end note]
19.7.41 ST_TLTimeNodeFillType (Time Node Fill Type)
This simple type specifies what modifications the effect leaves on the target element's properties when the
effect ends.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 2711\n\n--- Page 2722 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
freeze (Freeze) Freeze
hold (TimeNode Fill Type Enum ( Hold )) Hold
remove (Remove) Remove
transition (Transition) Transition
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeFillType) is located
in §A.3. end note]
19.7.42 ST_TLTimeNodeID (Time Node ID)
This simple type represents a node or event on the timeline by its identifier.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeID) is located in
§A.3. end note]
19.7.43 ST_TLTimeNodeMasterRelation (Time Node Master Relation)
This simple type specifies how the time node plays back relative to its master time node.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
lastClick (TimeNode Master Relation Enum ( Last Click Last Click
))
nextClick (TimeNode Master Relation Enum ( Next Next Click
Click ))
sameClick (TimeNode Master Relation Enum ( Same Same Click
Click ))
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeMasterRelation) is
located in §A.3. end note]
19.7.44 ST_TLTimeNodePresetClassType (Time Node Preset Class Type)
This simple type specifies the class of effect in which this effect belongs.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
2712 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2723 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
emph (Preset Type Enum ( Emphasis )) Emphasis Preset
entr (Preset Type Enum ( Entrance )) Entrance Preset
exit (Exit) Exit Preset
mediacall (Preset Type Enum ( Media Call )) Media Call Preset
path (Preset Type Enum ( Path )) Path Preset
verb (Preset Type Enum ( Verb )) Verb Preset
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodePresetClassType) is
located in §A.3. end note]
19.7.45 ST_TLTimeNodeRestartType (Time Node Restart Type)
This simple type determines whether an effect can play more than once.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
always (Restart Enum ( Always )) Always restart node
never (Restart Enum ( Never )) Never restart node
whenNotActive (Restart Enum ( When Not Active )) Restart when node is not active
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeRestartType) is
located in §A.3. end note]
19.7.46 ST_TLTimeNodeSyncType (Time Node Sync Type)
This simple type specifies how the time node synchronizes to its group.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
canSlip (TimeNode Sync Enum ( Can Slip )) Can Slip
locked (TimeNode Sync Enum ( Locked )) Locked
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeSyncType) is
located in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2713\n\n--- Page 2724 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.47 ST_TLTimeNodeType (Time Node Type)
This simple type specifies time node types.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
afterEffect (Node Type Enum ( After Effect )) After Effect
afterGroup (Node Type Enum ( After Group )) After Group
clickEffect (Node Type Enum ( Click Effect )) Click Effect
clickPar (Node Type Enum ( Click Paragraph )) Click Paragraph
interactiveSeq (Node Type Enum ( Interactive Interactive Sequence
Sequence ))
mainSeq (Node Type Enum ( Main Sequence )) Main Sequence
tmRoot (Node Type Enum ( Timing Root )) Timing Root
withEffect (Node Type Enum ( With Effect )) With Effect
withGroup (Node Type Enum ( With Group )) With Group
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTimeNodeType) is located in
§A.3. end note]
19.7.48 ST_TLTriggerEvent (Trigger Event)
This simple type specifies a particular event that causes the time condition to be true.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
begin (Trigger Event Enum ( Begin )) Fire trigger at the beginning
end (Trigger Event Enum ( End )) Fire trigger at the end
onBegin (Trigger Event Enum ( On Begin )) Fire trigger at the beginning
onClick (Trigger Event Enum ( On Click )) Fire trigger on a mouse click
onDblClick (Trigger Event Enum ( On Double Click )) Fire trigger on double-mouse click
onEnd (Trigger Event Enum ( On End )) Fire trigger at the end
onMouseOut (Trigger Event Enum ( On Mouse Out )) Fire trigger on mouse out
onMouseOver (Trigger Event Enum ( On Mouse Over Fire trigger on mouse over
))
onNext (Trigger Event Enum ( On Next )) Fire trigger on next node
2714 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2725 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
onPrev (Trigger Event Enum ( On Previous )) Fire trigger on previous node
onStopAudio (Trigger Event Enum ( On Stop Audio )) Fire trigger on stop audio
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTriggerEvent) is located in
§A.3. end note]
19.7.49 ST_TLTriggerRuntimeNode (Trigger RunTime Node)
This simple type specifies the child time node that triggers a time condition. References a child TimeNode or all
child nodes. Order is based on the child's end time.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
all (Trigger RunTime Node Enum ( All )) All
first (Trigger RunTime Node ( First )) First
last (Trigger RunTime Node ( Last )) Last
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLTriggerRuntimeNode) is
located in §A.3. end note]
19.7.50 ST_TransitionCornerDirectionType (Transition Corner Direction Type)
This simple type specifies diagonal directions for slide transitions.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
ld (Transition Corner Direction Enum ( Left-Down )) Specifies the slide transition direction of left-down
lu (Transition Corner Direction Enum ( Left-Up )) Specifies the slide transition direction of left-up
rd (Transition Corner Direction Enum ( Right-Down )) Specifies the slide transition direction of right-down
ru (Transition Corner Direction Enum ( Right-Up )) Specifies the slide transition direction of right-up
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TransitionCornerDirectionType)
is located in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2715\n\n--- Page 2726 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.51 ST_TransitionEightDirectionType (Transition Eight Direction)
This simple type specifies the direction of an animation.
This simple type is a union of the following types:
 The ST_TransitionCornerDirectionType simple type (§19.7.50).
 The ST_TransitionSideDirectionType simple type (§19.7.53).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TransitionEightDirectionType) is
located in §A.3. end note]
19.7.52 ST_TransitionInOutDirectionType (Transition In/Out Direction Type)
This simple type specifies if a slide transition should go in or out.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
in (Transition In/Out Direction Enum ( In )) Specifies the slide transition should go in
out (Transition In/Out Direction Enum ( Out )) Specifies the slide transition should go out
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TransitionInOutDirectionType) is
located in §A.3. end note]
19.7.53 ST_TransitionSideDirectionType (Transition Side Direction Type)
This simple type defines a set of slide transition directions.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
d (Transition Side Direction Enum ( Down )) Specifies that the transition direction is down
l (Transition Side Direction Enum ( Left )) Specifies that the transition direction is left
r (Transition Side Direction ( Right )) Specifies that the transition direction is right
u (Transition Side Direction Enum ( Up )) Specifies that the transition direction is up
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TransitionSideDirectionType) is
located in §A.3. end note]
2716 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2727 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.54 ST_TransitionSpeed (Transition Speed)
This simple type defines the allowed transition speeds for transitioning from the current slide to the next.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
fast (Fast) Fast slide transition.
med (Medium) Medium slide transition.
slow (low) Slow slide transition.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TransitionSpeed) is located in
§A.3. end note]
19.7.55 ST_ViewType (List of View Types)
This simple type defines the kinds of view available to an application when rendering a PresentationML
document. Those view kinds are, as follows: handout view, normal slide view, notes master view, notes view,
outline view, slide master view, slide sorter view, and slide thumbnail view. [Note: Although this Standard is for a
file format, occasionally, guidance is given regarding intent in dealing with things outside that file format, such
as the rendering of documents to a screen or printer. end note]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
handoutView (Handout Master View) Specifies that a given PresentationML document
should be rendered using some sort of template that is
intended to facilitate the changing of the design and
layout of printed handouts.
notesMasterView (Notes Master View) Specifies that a given PresentationML document
should be rendered using some sort of template that is
intended to facilitate the changing of the design and
layout of notes slides.
notesView (Notes View) Specifies that a given PresentationML document
should be rendered using some sort of template that is
intended to facilitate the viewing or editing of notes.
outlineView (Outline View) Specifies that a given PresentationML document
should be rendered in a view that is intended to
facilitate the viewing of slides in some outline form.
sldMasterView (Slide Master View) Specifies that a given PresentationML document
should be rendered using some sort of template that is
©ISO/IEC 2016 – All rights reserved 2717\n\n--- Page 2728 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
intended to facilitate the changing of the design and
layout of master slides.
sldSorterView (Slide Sorter View) Specifies that a given PresentationML document
should be rendered in a view that is intended to
facilitate the rearrangement of slides.
sldThumbnailView (Slide Thumbnail View) Specifies that a given PresentationML document
should be rendered in a view that shows slides in some
thumbnail form.
sldView (Normal Slide View) Specifies that a given PresentationML document
should be rendered in a view that allows slides to be
viewed or edited.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_ViewType) is located in §A.3.
end note]
2718 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2729 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20. DrawingML - Framework Reference
Material
[Note: For further information on the mapping of elements and attributes to OPC parts, see the Bibliography
entry, “Information on elements, attributes, and OPC parts in ISO/IEC 29500 (OOXML)”. end note]
The subordinate subclauses specify the semantics for the XML markup comprising DrawingML content, which
can be used within the contents of WordprocessingML, SpreadsheetML, or PresentationML documents.
This portion of DrawingML defines its core pieces.
20.1 DrawingML - Main
The DrawingML Main namespace defines all of the base constructs for all kinds of DrawingML objects (charts,
diagrams, shapes, pictures, and so on). These constructs and primitives are defined below.
20.1.1 Table of Contents
This subclause is informative.
20.1.2 Basics ......................................................................................................................................... 2727
20.1.2.1 EMU Unit of Measurement ......................................................................................................... 2727
20.1.2.2 Core Drawing Object Information ............................................................................................... 2727
20.1.2.2.1 bldChart (Build Chart) .............................................................................................................. 2727
20.1.2.2.2 bldDgm (Build Diagram) .......................................................................................................... 2728
20.1.2.2.3 chart (Chart to Animate) ......................................................................................................... 2729
20.1.2.2.4 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties) ............................................ 2729
20.1.2.2.5 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties) ................................... 2730
20.1.2.2.6 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties) ................................................... 2730
20.1.2.2.7 cNvPicPr (Non-Visual Picture Drawing Properties) ................................................................. 2730
20.1.2.2.8 cNvPr (Non-Visual Drawing Properties) .................................................................................. 2731
20.1.2.2.9 cNvSpPr (Non-Visual Shape Drawing Properties) .................................................................... 2733
20.1.2.2.10 cxnSp (Connection Shape) ................................................................................................... 2734
20.1.2.2.11 cxnSpLocks (Connection Shape Locks) ................................................................................ 2735
20.1.2.2.12 dgm (Diagram to Animate) .................................................................................................. 2737
20.1.2.2.13 endCxn (Connection End) .................................................................................................... 2737
20.1.2.2.14 ext (Extension) ..................................................................................................................... 2737
20.1.2.2.15 extLst (Extension List) .......................................................................................................... 2738
20.1.2.2.16 graphic (Graphic Object) ...................................................................................................... 2738
20.1.2.2.17 graphicData (Graphic Object Data) ..................................................................................... 2738
20.1.2.2.18 graphicFrame (Graphic Frame) ............................................................................................ 2739
20.1.2.2.19 graphicFrameLocks (Graphic Frame Locks) ......................................................................... 2739
20.1.2.2.20 grpSp (Group shape) ............................................................................................................ 2740
20.1.2.2.21 grpSpLocks (Group Shape Locks) ......................................................................................... 2741
©ISO/IEC 2016 – All rights reserved 2719\n\n--- Page 2730 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.2.22 grpSpPr (Visual Group Shape Properties) ............................................................................ 2742
20.1.2.2.23 hlinkHover (Hyperlink for Hover) ........................................................................................ 2743
20.1.2.2.24 ln (Outline) ........................................................................................................................... 2744
20.1.2.2.25 nvCxnSpPr (Non-Visual Properties for a Connection Shape)............................................... 2745
20.1.2.2.26 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame) ....................................... 2745
20.1.2.2.27 nvGrpSpPr (Non-Visual Properties for a Group Shape) ....................................................... 2745
20.1.2.2.28 nvPicPr (Non-Visual Properties for a Picture) ...................................................................... 2746
20.1.2.2.29 nvSpPr (Non-Visual Properties for a Shape) ........................................................................ 2746
20.1.2.2.30 pic (Picture) .......................................................................................................................... 2746
20.1.2.2.31 picLocks (Picture Locks) ....................................................................................................... 2747
20.1.2.2.32 snd (Hyperlink Sound) ......................................................................................................... 2749
20.1.2.2.33 sp (Shape) ............................................................................................................................ 2749
20.1.2.2.34 spLocks (Shape Locks) .......................................................................................................... 2750
20.1.2.2.35 spPr (Shape Properties) ....................................................................................................... 2751
20.1.2.2.36 stCxn (Connection Start) ...................................................................................................... 2752
20.1.2.2.37 style (Shape Style) ............................................................................................................... 2752
20.1.2.2.38 sx (Horizontal Ratio) ............................................................................................................ 2752
20.1.2.2.39 sy (Vertical Ratio) ................................................................................................................. 2753
20.1.2.2.40 txBody (Shape Text Body) .................................................................................................... 2753
20.1.2.2.41 txSp (Text Shape) ................................................................................................................. 2753
20.1.2.2.42 useSpRect (Use Shape Text Rectangle) ............................................................................... 2754
20.1.2.2.43 cpLocks (Content Part Locks) ............................................................................................... 2754
20.1.2.3 Colors ........................................................................................................................................... 2755
20.1.2.3.1 alpha (Alpha) ........................................................................................................................... 2755
20.1.2.3.2 alphaMod (Alpha Modulation) ................................................................................................ 2756
20.1.2.3.3 alphaOff (Alpha Offset) ............................................................................................................ 2757
20.1.2.3.4 blue (Blue) ............................................................................................................................... 2757
20.1.2.3.5 blueMod (Blue Modulation) .................................................................................................... 2758
20.1.2.3.6 blueOff (Blue Offset) ................................................................................................................ 2758
20.1.2.3.7 comp (Complement) ................................................................................................................ 2759
20.1.2.3.8 gamma (Gamma) ..................................................................................................................... 2760
20.1.2.3.9 gray (Gray) ............................................................................................................................... 2760
20.1.2.3.10 green (Green) ...................................................................................................................... 2760
20.1.2.3.11 greenMod (Green Modulation) ........................................................................................... 2760
20.1.2.3.12 greenOff (Green Offset) ....................................................................................................... 2761
20.1.2.3.13 hslClr (Hue, Saturation, Luminance Color Model) ............................................................... 2762
20.1.2.3.14 hue (Hue) ............................................................................................................................. 2762
20.1.2.3.15 hueMod (Hue Modulate) ..................................................................................................... 2763
20.1.2.3.16 hueOff (Hue Offset) ............................................................................................................. 2764
20.1.2.3.17 inv (Inverse) ......................................................................................................................... 2764
20.1.2.3.18 invGamma (Inverse Gamma) ............................................................................................... 2765
20.1.2.3.19 lum (Luminance) .................................................................................................................. 2765
20.1.2.3.20 lumMod (Luminance Modulation) ...................................................................................... 2766
20.1.2.3.21 lumOff (Luminance Offset) .................................................................................................. 2766
20.1.2.3.22 prstClr (Preset Color) ........................................................................................................... 2767
20.1.2.3.23 red (Red) .............................................................................................................................. 2767
20.1.2.3.24 redMod (Red Modulation) ................................................................................................... 2768
20.1.2.3.25 redOff (Red Offset) .............................................................................................................. 2768
2720 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2731 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.26 sat (Saturation) .................................................................................................................... 2769
20.1.2.3.27 satMod (Saturation Modulation) ......................................................................................... 2770
20.1.2.3.28 satOff (Saturation Offset) .................................................................................................... 2771
20.1.2.3.29 schemeClr (Scheme Color) ................................................................................................... 2771
20.1.2.3.30 scrgbClr (RGB Color Model - Percentage Variant) ............................................................... 2772
20.1.2.3.31 shade (Shade) ...................................................................................................................... 2772
20.1.2.3.32 srgbClr (RGB Color Model - Hex Variant) ............................................................................. 2773
20.1.2.3.33 sysClr (System Color) ........................................................................................................... 2774
20.1.2.3.34 tint (Tint) .............................................................................................................................. 2774
20.1.3 Audio and Video ......................................................................................................................... 2775
20.1.3.1 audioCd (Audio from CD) ............................................................................................................. 2775
20.1.3.2 audioFile (Audio from File) .......................................................................................................... 2776
20.1.3.3 end (Audio End Time) .................................................................................................................. 2777
20.1.3.4 quickTimeFile (QuickTime from File) ........................................................................................... 2778
20.1.3.5 st (Audio Start Time) .................................................................................................................... 2779
20.1.3.6 videoFile (Video from File) .......................................................................................................... 2779
20.1.3.7 wavAudioFile (Audio from WAV File) .......................................................................................... 2780
20.1.4 Styles ......................................................................................................................................... 2782
20.1.4.1 Styles ............................................................................................................................................ 2782
20.1.4.1.1 accent1 (Accent 1) ................................................................................................................... 2782
20.1.4.1.2 accent2 (Accent 2) ................................................................................................................... 2782
20.1.4.1.3 accent3 (Accent 3) ................................................................................................................... 2783
20.1.4.1.4 accent4 (Accent 4) ................................................................................................................... 2784
20.1.4.1.5 accent5 (Accent 5) ................................................................................................................... 2784
20.1.4.1.6 accent6 (Accent 6) ................................................................................................................... 2785
20.1.4.1.7 bgFillStyleLst (Background Fill Style List) ................................................................................. 2785
20.1.4.1.8 custClr (Custom color) ............................................................................................................. 2786
20.1.4.1.9 dk1 (Dark 1) ............................................................................................................................. 2786
20.1.4.1.10 dk2 (Dark 2) ......................................................................................................................... 2787
20.1.4.1.11 effectStyle (Effect Style) ...................................................................................................... 2788
20.1.4.1.12 effectStyleLst (Effect Style List) ........................................................................................... 2788
20.1.4.1.13 fillStyleLst (Fill Style List) ...................................................................................................... 2789
20.1.4.1.14 fmtScheme (Format Scheme) .............................................................................................. 2790
20.1.4.1.15 folHlink (Followed Hyperlink) .............................................................................................. 2791
20.1.4.1.16 font (Font) ............................................................................................................................ 2791
20.1.4.1.17 fontRef (Font Reference) ..................................................................................................... 2792
20.1.4.1.18 fontScheme (Font Scheme) ................................................................................................. 2792
20.1.4.1.19 hlink (Hyperlink) .................................................................................................................. 2793
20.1.4.1.20 lnDef (Line Default) .............................................................................................................. 2794
20.1.4.1.21 lnStyleLst (Line Style List) .................................................................................................... 2794
20.1.4.1.22 lt1 (Light 1) ........................................................................................................................... 2795
20.1.4.1.23 lt2 (Light 2) ........................................................................................................................... 2796
20.1.4.1.24 majorFont (Major Font) ....................................................................................................... 2797
20.1.4.1.25 minorFont (Minor fonts) ...................................................................................................... 2797
20.1.4.1.26 scene3d (3D Scene Properties) ............................................................................................ 2798
20.1.4.1.27 spDef (Shape Default) .......................................................................................................... 2798
20.1.4.1.28 txDef (Text Default) ............................................................................................................. 2799
©ISO/IEC 2016 – All rights reserved 2721\n\n--- Page 2732 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2 Table Styles .................................................................................................................................. 2800
20.1.4.2.1 band1H (Band 1 Horizontal) .................................................................................................... 2800
20.1.4.2.2 band1V (Band 1 Vertical) ......................................................................................................... 2801
20.1.4.2.3 band2H (Band 2 Horizontal) .................................................................................................... 2802
20.1.4.2.4 band2V (Band 2 Vertical) ......................................................................................................... 2803
20.1.4.2.5 bevel (Bevel) ............................................................................................................................ 2804
20.1.4.2.6 bottom (Bottom Border) ......................................................................................................... 2805
20.1.4.2.7 effect (Effect) ........................................................................................................................... 2805
20.1.4.2.8 effectRef (Effect Reference) .................................................................................................... 2805
20.1.4.2.9 fill (Fill) ..................................................................................................................................... 2806
20.1.4.2.10 fillRef (Fill Reference) .......................................................................................................... 2807
20.1.4.2.11 firstCol (First Column) .......................................................................................................... 2807
20.1.4.2.12 firstRow (First Row) ............................................................................................................. 2808
20.1.4.2.13 font (Font) ............................................................................................................................ 2809
20.1.4.2.14 insideH (Inside Horizontal Border) ...................................................................................... 2809
20.1.4.2.15 insideV (Inside Vertical Border) ........................................................................................... 2810
20.1.4.2.16 lastCol (Last Column) ........................................................................................................... 2810
20.1.4.2.17 lastRow (Last Row) .............................................................................................................. 2811
20.1.4.2.18 left (Left Border) .................................................................................................................. 2812
20.1.4.2.19 lnRef (Line Reference) ......................................................................................................... 2813
20.1.4.2.20 neCell (Northeast Cell) ......................................................................................................... 2813
20.1.4.2.21 nwCell (Northwest Cell) ....................................................................................................... 2814
20.1.4.2.22 right (Right Border) .............................................................................................................. 2814
20.1.4.2.23 seCell (Southeast Cell) ......................................................................................................... 2815
20.1.4.2.24 swCell (Southwest Cell) ....................................................................................................... 2815
20.1.4.2.25 tblBg (Table Background) .................................................................................................... 2816
20.1.4.2.26 tblStyle (Table Style) ............................................................................................................ 2817
20.1.4.2.27 tblStyleLst (Table Style List) ................................................................................................. 2817
20.1.4.2.28 tcBdr (Table Cell Borders) .................................................................................................... 2818
20.1.4.2.29 tcStyle (Table Cell Style) ...................................................................................................... 2819
20.1.4.2.30 tcTxStyle (Table Cell Text Style) ........................................................................................... 2819
20.1.4.2.31 tl2br (Top Left to Bottom Right Border) .............................................................................. 2820
20.1.4.2.32 top (Top Border) .................................................................................................................. 2820
20.1.4.2.33 tr2bl (Top Right to Bottom Left Border) .............................................................................. 2821
20.1.4.2.34 wholeTbl (Whole Table) ...................................................................................................... 2821
20.1.5 3D .............................................................................................................................................. 2821
20.1.5.1 anchor (Anchor Point) ................................................................................................................. 2822
20.1.5.2 backdrop (Backdrop Plane) ......................................................................................................... 2822
20.1.5.3 bevelB (Bottom Bevel) ................................................................................................................. 2823
20.1.5.4 bevelT (Top Bevel) ....................................................................................................................... 2824
20.1.5.5 camera (Camera) ......................................................................................................................... 2825
20.1.5.6 contourClr (Contour Color) .......................................................................................................... 2827
20.1.5.7 extrusionClr (Extrusion Color) ..................................................................................................... 2828
20.1.5.8 flatTx (No text in 3D scene) ......................................................................................................... 2829
20.1.5.9 lightRig (Light Rig) ........................................................................................................................ 2829
20.1.5.10 norm (Normal) ............................................................................................................................. 2830
20.1.5.11 rot (Rotation) ............................................................................................................................... 2831
2722 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2733 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.5.12 sp3d (Apply 3D shape properties) ............................................................................................... 2832
20.1.5.13 up (Up Vector) ............................................................................................................................. 2834
20.1.6 Shared Style Sheet ...................................................................................................................... 2835
20.1.6.1 clrMap (Color Map) ..................................................................................................................... 2836
20.1.6.2 clrScheme (Color Scheme) ........................................................................................................... 2837
20.1.6.3 custClrLst (Custom Color List) ...................................................................................................... 2839
20.1.6.4 extraClrScheme (Extra Color Scheme) ......................................................................................... 2839
20.1.6.5 extraClrSchemeLst (Extra Color Scheme List) .............................................................................. 2840
20.1.6.6 masterClrMapping (Master Color Mapping) ............................................................................... 2841
20.1.6.7 objectDefaults (Object Defaults) ................................................................................................. 2841
20.1.6.8 overrideClrMapping (Override Color Mapping) .......................................................................... 2841
20.1.6.9 theme (Theme) ............................................................................................................................ 2843
20.1.6.10 themeElements (Theme Elements) ............................................................................................. 2843
20.1.6.11 themeManager (Theme Manager) .............................................................................................. 2844
20.1.6.12 themeOverride (Theme Override) ............................................................................................... 2844
20.1.7 Coordinate Systems and Transformations ................................................................................... 2845
20.1.7.1 chExt (Child Extents) .................................................................................................................... 2845
20.1.7.2 chOff (Child Offset) ...................................................................................................................... 2845
20.1.7.3 ext (Extents) ................................................................................................................................. 2846
20.1.7.4 off (Offset) ................................................................................................................................... 2847
20.1.7.5 xfrm (2D Transform for Grouped Objects) .................................................................................. 2848
20.1.7.6 xfrm (2D Transform for Individual Objects) ................................................................................. 2849
20.1.8 Shape Fills, Effects, and Line Properties ....................................................................................... 2850
20.1.8.1 alphaBiLevel (Alpha Bi-Level Effect) ............................................................................................ 2850
20.1.8.2 alphaCeiling (Alpha Ceiling Effect) ............................................................................................... 2850
20.1.8.3 alphaFloor (Alpha Floor Effect) .................................................................................................... 2850
20.1.8.4 alphaInv (Alpha Inverse Effect) .................................................................................................... 2850
20.1.8.5 alphaMod (Alpha Modulate Effect) ............................................................................................. 2851
20.1.8.6 alphaModFix (Alpha Modulate Fixed Effect) ............................................................................... 2851
20.1.8.7 alphaOutset (Alpha Inset/Outset Effect) ..................................................................................... 2851
20.1.8.8 alphaRepl (Alpha Replace Effect) ................................................................................................ 2852
20.1.8.9 bevel (Line Join Bevel) ................................................................................................................. 2852
20.1.8.10 bgClr (Background color) ............................................................................................................. 2852
20.1.8.11 biLevel (Bi-Level (Black/White) Effect) ........................................................................................ 2852
20.1.8.12 blend (Blend Effect) ..................................................................................................................... 2853
20.1.8.13 blip (Blip) ...................................................................................................................................... 2853
20.1.8.14 blipFill (Picture Fill) ...................................................................................................................... 2854
20.1.8.15 blur (Blur Effect) .......................................................................................................................... 2856
20.1.8.16 clrChange (Color Change Effect) .................................................................................................. 2857
20.1.8.17 clrFrom (Change Color From) ...................................................................................................... 2858
20.1.8.18 clrRepl (Solid Color Replacement) ............................................................................................... 2858
20.1.8.19 clrTo (Change Color To) ............................................................................................................... 2858
20.1.8.20 cont (Effect Container) ................................................................................................................ 2858
20.1.8.21 custDash (Custom Dash) .............................................................................................................. 2858
20.1.8.22 ds (Dash Stop) .............................................................................................................................. 2859
20.1.8.23 duotone (Duotone Effect) ........................................................................................................... 2859
©ISO/IEC 2016 – All rights reserved 2723\n\n--- Page 2734 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.24 effect (Effect) ............................................................................................................................... 2859
20.1.8.25 effectDag (Effect Container) ........................................................................................................ 2860
20.1.8.26 effectLst (Effect Container).......................................................................................................... 2860
20.1.8.27 fgClr (Foreground color) .............................................................................................................. 2862
20.1.8.28 fill (Fill) ......................................................................................................................................... 2863
20.1.8.29 fillOverlay (Fill Overlay Effect) ..................................................................................................... 2863
20.1.8.30 fillRect (Fill Rectangle) ................................................................................................................. 2863
20.1.8.31 fillToRect (Fill To Rectangle) ........................................................................................................ 2864
20.1.8.32 glow (Glow Effect) ....................................................................................................................... 2866
20.1.8.33 gradFill (Gradient Fill) .................................................................................................................. 2866
20.1.8.34 grayscl (Gray Scale Effect) ........................................................................................................... 2868
20.1.8.35 grpFill (Group Fill) ........................................................................................................................ 2868
20.1.8.36 gs (Gradient stops)....................................................................................................................... 2868
20.1.8.37 gsLst (Gradient Stop List) ............................................................................................................. 2868
20.1.8.38 headEnd (Line Head/End Style) ................................................................................................... 2868
20.1.8.39 hsl (Hue Saturation Luminance Effect) ........................................................................................ 2869
20.1.8.40 innerShdw (Inner Shadow Effect) ................................................................................................ 2870
20.1.8.41 lin (Linear Gradient Fill) ............................................................................................................... 2870
20.1.8.42 lum (Luminance Effect) ................................................................................................................ 2871
20.1.8.43 miter (Miter Line Join) ................................................................................................................. 2871
20.1.8.44 noFill (No Fill) ............................................................................................................................... 2872
20.1.8.45 outerShdw (Outer Shadow Effect) .............................................................................................. 2872
20.1.8.46 path (Path Gradient) .................................................................................................................... 2873
20.1.8.47 pattFill (Pattern Fill) ..................................................................................................................... 2874
20.1.8.48 prstDash (Preset Dash) ................................................................................................................ 2874
20.1.8.49 prstShdw (Preset Shadow) .......................................................................................................... 2875
20.1.8.50 reflection (Reflection Effect) ....................................................................................................... 2875
20.1.8.51 relOff (Relative Offset Effect) ...................................................................................................... 2878
20.1.8.52 round (Round Line Join) ............................................................................................................... 2878
20.1.8.53 softEdge (Soft Edge Effect) .......................................................................................................... 2878
20.1.8.54 solidFill (Solid Fill) ........................................................................................................................ 2879
20.1.8.55 srcRect (Source Rectangle) .......................................................................................................... 2879
20.1.8.56 stretch (Stretch) ........................................................................................................................... 2879
20.1.8.57 tailEnd (Tail line end style) .......................................................................................................... 2880
20.1.8.58 tile (Tile) ....................................................................................................................................... 2880
20.1.8.59 tileRect (Tile Rectangle) ............................................................................................................... 2882
20.1.8.60 tint (Tint Effect) ........................................................................................................................... 2883
20.1.8.61 xfrm (Transform Effect) ............................................................................................................... 2883
20.1.9 Shape Definitions and Attributes ................................................................................................ 2884
20.1.9.1 ahLst (List of Shape Adjust Handles) ........................................................................................... 2885
20.1.9.2 ahPolar (Polar Adjust Handle) ..................................................................................................... 2885
20.1.9.3 ahXY (XY Adjust Handle) .............................................................................................................. 2886
20.1.9.4 arcTo (Draw Arc To) ..................................................................................................................... 2887
20.1.9.5 avLst (List of Shape Adjust Values) .............................................................................................. 2889
20.1.9.6 close (Close Shape Path) .............................................................................................................. 2890
20.1.9.7 cubicBezTo (Draw Cubic Bezier Curve To) ................................................................................... 2891
20.1.9.8 custGeom (Custom Geometry) .................................................................................................... 2892
2724 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2735 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.9.9 cxn (Shape Connection Site) ........................................................................................................ 2893
20.1.9.10 cxnLst (List of Shape Connection Sites) ....................................................................................... 2895
20.1.9.11 gd (Shape Guide) ......................................................................................................................... 2895
20.1.9.12 gdLst (List of Shape Guides) ......................................................................................................... 2898
20.1.9.13 lnTo (Draw Line To) ...................................................................................................................... 2898
20.1.9.14 moveTo (Move Path To) .............................................................................................................. 2899
20.1.9.15 path (Shape Path) ........................................................................................................................ 2899
20.1.9.16 pathLst (List of Shape Paths) ....................................................................................................... 2901
20.1.9.17 pos (Shape Position Coordinate) ................................................................................................. 2902
20.1.9.18 prstGeom (Preset geometry) ....................................................................................................... 2904
20.1.9.19 prstTxWarp (Preset Text Warp) ................................................................................................... 2905
20.1.9.20 pt (Shape Path Point) ................................................................................................................... 2908
20.1.9.21 quadBezTo (Draw Quadratic Bezier Curve To) ............................................................................ 2910
20.1.9.22 rect (Shape Text Rectangle) ......................................................................................................... 2910
20.1.10 Simple Types ......................................................................................................................... 2911
20.1.10.1 ST_AdjAngle (Adjustable Angle Methods) ................................................................................... 2911
20.1.10.2 ST_AdjCoordinate (Adjustable Coordinate Methods) ................................................................. 2911
20.1.10.3 ST_Angle (Angle) .......................................................................................................................... 2912
20.1.10.4 ST_AnimationBuildType (Animation Build Type) ........................................................................ 2912
20.1.10.5 ST_AnimationChartBuildType (Chart Animation Build Type) ...................................................... 2912
20.1.10.6 ST_AnimationChartOnlyBuildType (Chart only Animation Types) .............................................. 2912
20.1.10.7 ST_AnimationDgmBuildType (Diagram Animation Build Type) .................................................. 2913
20.1.10.8 ST_AnimationDgmOnlyBuildType (Diagram only Animation Types) ........................................... 2913
20.1.10.9 ST_BevelPresetType (Bevel Presets) ........................................................................................... 2914
20.1.10.10 ST_BlackWhiteMode (Black and White Mode) ....................................................................... 2918
20.1.10.11 ST_BlendMode (Blend Mode) ................................................................................................. 2919
20.1.10.12 ST_BlipCompression (Blip Compression Type) ........................................................................ 2919
20.1.10.13 ST_ChartBuildStep (Chart Animation Build Step) .................................................................... 2919
20.1.10.14 ST_ColorSchemeIndex (Theme Color Reference) .................................................................... 2920
20.1.10.15 ST_CompoundLine (Compound Line Type) ............................................................................. 2921
20.1.10.16 ST_Coordinate (Coordinate) .................................................................................................... 2921
20.1.10.17 ST_Coordinate32 (Coordinate Point) ...................................................................................... 2921
20.1.10.18 ST_Coordinate32Unqualified (Coordinate Point) .................................................................... 2922
20.1.10.19 ST_CoordinateUnqualified (Coordinate) ................................................................................. 2922
20.1.10.20 ST_DgmBuildStep (Diagram Animation Build Steps) ............................................................... 2922
20.1.10.21 ST_DrawingElementId (Drawing Element ID) .......................................................................... 2922
20.1.10.22 ST_EffectContainerType (Effect Container Type) .................................................................... 2923
20.1.10.23 ST_FixedAngle (Fixed Angle) .................................................................................................... 2923
20.1.10.24 ST_FixedPercentage (Fixed Percentage) ................................................................................. 2924
20.1.10.25 ST_FontCollectionIndex (Font Collection Index) ..................................................................... 2924
20.1.10.26 ST_FOVAngle (Field of View Angle) ......................................................................................... 2924
20.1.10.27 ST_GeomGuideFormula (Geometry Guide Formula Properties) ............................................ 2924
20.1.10.28 ST_GeomGuideName (Geometry Guide Name Properties) .................................................... 2925
20.1.10.29 ST_LightRigDirection (Light Rig Direction) ............................................................................... 2925
20.1.10.30 ST_LightRigType (Light Rig Type) ............................................................................................. 2929
20.1.10.31 ST_LineCap (End Line Cap) ...................................................................................................... 2938
20.1.10.32 ST_LineEndLength (Line End Length) ...................................................................................... 2938
©ISO/IEC 2016 – All rights reserved 2725\n\n--- Page 2736 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.33 ST_LineEndType (Line End Type) ............................................................................................. 2939
20.1.10.34 ST_LineEndWidth (Line End Width) ......................................................................................... 2939
20.1.10.35 ST_LineWidth (Line Width) ...................................................................................................... 2940
20.1.10.36 ST_OnOffStyleType (On/Off Style Type) .................................................................................. 2940
20.1.10.37 ST_PathFillMode (Path Fill Mode) ........................................................................................... 2941
20.1.10.38 ST_PathShadeType (Path Shade Type) .................................................................................... 2941
20.1.10.39 ST_PenAlignment (Alignment Type) ........................................................................................ 2941
20.1.10.40 ST_Percentage (Percentage) ................................................................................................... 2942
20.1.10.41 ST_PitchFamily (Pitch Family) .................................................................................................. 2942
20.1.10.42 ST_PositiveCoordinate (Positive Coordinate) .......................................................................... 2943
20.1.10.43 ST_PositiveCoordinate32 (Positive Coordinate Point) ............................................................ 2943
20.1.10.44 ST_PositiveFixedAngle (Positive Fixed Angle) ......................................................................... 2944
20.1.10.45 ST_PositiveFixedPercentage (Positive Fixed Percentage) ....................................................... 2944
20.1.10.46 ST_PositivePercentage (Positive Percentage Value with Sign) ............................................... 2944
20.1.10.47 ST_PresetCameraType (Preset Camera Type) ......................................................................... 2944
20.1.10.48 ST_PresetColorVal (Preset Color Value) .................................................................................. 2965
20.1.10.49 ST_PresetLineDashVal (Preset Line Dash Value) ..................................................................... 2971
20.1.10.50 ST_PresetMaterialType (Preset Material Type) ...................................................................... 2972
20.1.10.51 ST_PresetPatternVal (Preset Pattern Value) ........................................................................... 2981
20.1.10.52 ST_PresetShadowVal (Preset Shadow Type) ........................................................................... 2984
20.1.10.53 ST_RectAlignment (Rectangle Alignments) ............................................................................. 2987
20.1.10.54 ST_SchemeColorVal (Scheme Color) ....................................................................................... 2987
20.1.10.55 ST_ShapeID (Shape ID) ............................................................................................................ 2988
20.1.10.56 ST_ShapeType (Preset Shape Types) ....................................................................................... 2988
20.1.10.57 ST_StyleMatrixColumnIndex (Style Matrix Column Index) ..................................................... 3057
20.1.10.58 ST_SystemColorVal (System Color Value) ............................................................................... 3057
20.1.10.59 ST_TextAlignType (Text Alignment Types) .............................................................................. 3059
20.1.10.60 ST_TextAnchoringType (Text Anchoring Types) ...................................................................... 3060
20.1.10.61 ST_TextAutonumberScheme (Text Auto-number Schemes)................................................... 3060
20.1.10.62 ST_TextBulletSizePercent (Bullet Size Percentage) ................................................................. 3063
20.1.10.63 ST_TextBulletStartAtNum (Start Bullet At Number) ............................................................... 3063
20.1.10.64 ST_TextCapsType (Text Cap Types) ......................................................................................... 3063
20.1.10.65 ST_TextColumnCount (Text Column Count) ............................................................................ 3064
20.1.10.66 ST_TextFontAlignType (Font Alignment Types) ...................................................................... 3064
20.1.10.67 ST_TextFontScalePercentOrPercentString (Text Font Scale Percentage) ............................... 3065
20.1.10.68 ST_TextFontSize (Text Font Size) ............................................................................................. 3065
20.1.10.69 ST_TextHorzOverflowType (Text Horizontal Overflow Types) ................................................ 3065
20.1.10.70 ST_TextIndent (Text Indentation)............................................................................................ 3065
20.1.10.71 ST_TextIndentLevelType (Text Indent Level Type) .................................................................. 3066
20.1.10.72 ST_TextMargin (Text Margin) .................................................................................................. 3066
20.1.10.73 ST_TextNonNegativePoint (Text Non-Negative Point) ............................................................ 3066
20.1.10.74 ST_TextPoint (Text Point) ........................................................................................................ 3067
20.1.10.75 ST_TextPointUnqualified (Text Point) ..................................................................................... 3067
20.1.10.76 ST_TextShapeType (Preset Text Shape Types) ........................................................................ 3067
20.1.10.77 ST_TextSpacingPercentOrPercentString (Text Spacing Percent) ............................................ 3081
20.1.10.78 ST_TextSpacingPoint (Text Spacing Point) .............................................................................. 3081
20.1.10.79 ST_TextStrikeType (Text Strike Type) ...................................................................................... 3082
20.1.10.80 ST_TextTabAlignType (Text Tab Alignment Types) ................................................................. 3082
2726 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2737 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.81 ST_TextTypeface (Text Typeface) ............................................................................................ 3082
20.1.10.82 ST_TextUnderlineType (Text Underline Types) ....................................................................... 3083
20.1.10.83 ST_TextVerticalType (Vertical Text Types) .............................................................................. 3084
20.1.10.84 ST_TextVertOverflowType (Text Vertical Overflow) ............................................................... 3085
20.1.10.85 ST_TextWrappingType (Text Wrapping Types) ....................................................................... 3085
20.1.10.86 ST_TileFlipMode (Tile Flip Mode) ............................................................................................ 3085
20.1.10.87 ST_TextBulletSize (Bullet Size Percentage) ............................................................................. 3087
End of informative text.
20.1.2 Basics
This section describes all the basic common elements associated with the DrawingML framework.
20.1.2.1 EMU Unit of Measurement
Throughout ISO/IEC 29500, the EMU is used as a unit of measurement for length. An EMU is defined as follows:
1 1
1 emu= US inch= cm
914400 360000
[Rationale: The EMU was created in order to be able to evenly divide in both English and Metric units, in order
to avoid rounding errors during the calculation. The usage of EMUs also facilitates a more seamless system
switch and interoperability between different locales utilizing different units of measurement. EMUs define an
integer based, high precision coordinate system. end rationale]
20.1.2.2 Core Drawing Object Information
Within DrawingML, there is the notion of core drawing elements. These are elements that both are vital to and
common across the DrawingML framework. These elements denote the most integral pieces of the DrawingML
document structure and thus are among the most widely used.
[Note: Measurement Units - Length units must be expressed in device-independent physical units: English
Metric units (EMUs), points, picas, and inches. Device-dependent units such as pixels must not be used. end
note]
20.1.2.2.1 bldChart (Build Chart)
This element specifies how to build the animation for a diagram.
[Example: Consider the following example where a chart is specified to be animated by category rather than as
one entity. Thus, the bldChart element should be used as follows:
©ISO/IEC 2016 – All rights reserved 2727\n\n--- Page 2738 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:bdldLst>
<p:bldGraphic spid="4" grpId="0">
<p:bldSub>
<a:bldChart bld="category"/>
</p:bldSub>
</p:bldGraphic>
</p:bldLst>
end example]
Attributes Description
animBg (Animate Specifies whether or not the chart background elements should be animated as well.
Background) [Note: An example of background elements are grid lines and the chart legend. end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bld (Build) Specifies how the chart is built. The animation animates the sub-elements in the
container in the particular order defined by this attribute.
The possible values for this attribute are defined by the ST_AnimationChartBuildType
simple type (§20.1.10.5).
[Note: The W3C XML Schema definition of this element’s content model (CT_AnimationChartBuildProperties) is
located in §A.4.1. end note]
20.1.2.2.2 bldDgm (Build Diagram)
This element specifies how to build the animation for a diagram.
[Example: Consider having a diagram appear as on entity as opposed to by section. The bldDgm element should
be used as follows:
<p:bdldLst>
<p:bldGraphic spid="4" grpId="0">
<p:bldSub>
<a:bldDgm bld="one"/>
</p:bldSub>
</p:bldGraphic>
</p:bldLst>
end example]
Attributes Description
bld (Build) Specifies how the chart is built. The animation animates the sub-elements in the
container in the particular order defined by this attribute.
2728 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2739 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_AnimationDgmBuildType
simple type (§20.1.10.7).
rev (Reverse Specifies whether the animation of the objects in this diagram should be reversed or not.
Animation) If this attribute is not specified, a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_AnimationDgmBuildProperties) is
located in §A.4.1. end note]
20.1.2.2.3 chart (Chart to Animate)
This element specifies a reference to a chart that should be animated within a sequence of slide animations. In
addition to simply acting as a reference to a chart there is also animation build steps defined.
Attributes Description
bldStep (Animation Specifies which step this part of the chart should be built using. For instance the chart can
Build Step) be built as one object meaning it is animated as a single graphic. Alternatively the chart
can be animated, or built as separate pieces.
The possible values for this attribute are defined by the ST_ChartBuildStep simple type
(§20.1.10.13).
categoryIdx Specifies the index of the category within the corresponding chart that should be
(Category Index) animated.
The possible values for this attribute are defined by the W3C XML Schema int datatype.
seriesIdx (Series Specifies the index of the series within the corresponding chart that should be animated.
Index)
The possible values for this attribute are defined by the W3C XML Schema int datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_AnimationChartElement) is located
in §A.4.1. end note]
20.1.2.2.4 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties)
This element specifies the non-visual drawing properties for a connector shape. These non-visual properties are
properties that the generating application would utilize when rendering the slide surface.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualConnectorProperties) is
located in §A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2729\n\n--- Page 2740 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.2.5 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties)
This element specifies the non-visual drawing properties for a graphic frame. These non-visual properties are
properties that the generating application would utilize when rendering the slide surface.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualGraphicFrameProperties)
is located in §A.4.1. end note]
20.1.2.2.6 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties)
This element specifies the non-visual drawing properties for a group shape. These non-visual properties are
properties that the generating application would utilize when rendering the slide surface.
[Note: The W3C XML Schema definition of this element’s content model
(CT_NonVisualGroupDrawingShapeProps) is located in §A.4.1. end note]
20.1.2.2.7 cNvPicPr (Non-Visual Picture Drawing Properties)
This element specifies the non-visual properties for the picture canvas. These properties are to be used by the
generating application to determine how certain properties are to be changed for the picture object in question.
[Example: Consider the following DrawingML.
<p:pic>
…
<p:nvPicPr>
<p:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
<p:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</p:cNvPicPr>
<p:nvPr/>
</p:nvPicPr>
…
</p:pic>
end example]
Attributes Description
preferRelativeResi Specifies if the user interface should show the resizing of the picture based on the
ze (Relative Resize picture's current size or its original size. If this attribute is set to true, then scaling is
Preferred) relative to the original picture size as opposed to the current picture size.
[Example: Consider the case where a picture has been resized within a document and is
now 50% of the originally inserted picture size. Now if the user chooses to make a later
adjustment to the size of this picture within the generating application, then the value of
this attribute should be checked.
If this attribute is set to true then a value of 50% is shown. Similarly, if this attribute is set
2730 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2741 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
to false, then a value of 100% should be shown because the picture has not yet been
resized from its current (smaller) size. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualPictureProperties) is
located in §A.4.1. end note]
20.1.2.2.8 cNvPr (Non-Visual Drawing Properties)
This element specifies non-visual canvas properties. This allows for additional information that does not affect
the appearance of the picture to be stored.
[Example: Consider the following DrawingML.
<p:pic>
…
<p:nvPicPr>
<p:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
</p:nvPicPr>
…
</p:pic>
end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications which do not display the current object.
If this element is omitted, then no alternative text is present for the parent object.
[Example: Consider a DrawingML object defined as follows:
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text which can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
This attribute determines whether the object is rendered or made hidden. [Note: An
©ISO/IEC 2016 – All rights reserved 2731\n\n--- Page 2742 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
application can have settings which allow this object to be viewed. end note]
If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
[Example: Consider an inline DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
If multiple objects within the same document share the same id attribute value, then the
document shall be considered non-conformant.
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
[Example: Consider a DrawingML object defined as follows:
< … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
2732 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2743 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
If this attribute is omitted, then no title text is present for the parent object.
[Example: Consider a DrawingML object defined as follows:
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
20.1.2.2.9 cNvSpPr (Non-Visual Shape Drawing Properties)
This element specifies the non-visual drawing properties for a shape. These properties are to be used by the
generating application to determine how the shape should be dealt with
[Example: Consider the shape that has a shape lock applied to it.
<p:sp>
<p:nvSpPr>
<p:cNvPr id="2" name="Rectangle 1"/>
<p:cNvSpPr>
<a:spLocks noGrp="1"/>
</p:cNvSpPr>
</p:nvSpPr>
…
</p:sp>
This shape lock is stored within the non-visual drawing properties for this shape. end example]
Attributes Description
txBox (Text Box) Specifies that the corresponding shape is a text box and thus should be treated as such
by the generating application. If this attribute is omitted then it is assumed that the
corresponding shape is not specifically a text box.
[Note: Because a shape is not specified to be a text box does not mean that it cannot
have text attached to it. A text box is merely a specialized shape with specific properties.
end note]
©ISO/IEC 2016 – All rights reserved 2733\n\n--- Page 2744 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingShapeProps) is
located in §A.4.1. end note]
20.1.2.2.10 cxnSp (Connection Shape)
This element specifies a connection shape that is used to connect two sp elements. Once a connection is
specified using a cxnSp, it is left to the generating application to determine the exact path the connector takes.
That is the connector routing algorithm is left up to the generating application as the desired path might be
different depending on the specific needs of the application.
[Example: Consider the following connector shape that connects two regular shapes.
<p:spTree>
…
<p:sp>
<p:nvSpPr>
<p:cNvPr id="1" name="Rectangle 1"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
…
</p:sp>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="2" name="Rectangle 2"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
…
</p:sp>
<p:cxnSp>
2734 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2745 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:nvCxnSpPr>
<p:cNvPr id="3" name="Elbow Connector 3"/>
<p:cNvCxnSpPr>
<a:stCxn id="1" idx="3"/>
<a:endCxn id="2" idx="1"/>
</p:cNvCxnSpPr>
<p:nvPr/>
</p:nvCxnSpPr>
…
</p:cxnSp>
</p:spTree>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlConnector) is located in
§A.4.1. end note]
20.1.2.2.11 cxnSpLocks (Connection Shape Locks)
This element specifies all locking properties for a connection shape. These properties inform the generating
application about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noAdjustHandles Specifies that the generating application should not show adjust handles for the
(Disallow Showing corresponding connection shape. If this attribute is not specified, then a value of false is
Adjust Handles) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeArrowhe Specifies that the generating application should not allow arrowhead changes for the
ads (Disallow corresponding connection shape. If this attribute is not specified, then a value of false is
Arrowhead assumed.
Changes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding connection shape. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeShapeTy Specifies that the generating application should not allow shape type changes for the
pe (Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Type Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
©ISO/IEC 2016 – All rights reserved 2735\n\n--- Page 2746 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
datatype.
noEditPoints Specifies that the generating application should not allow shape point changes for the
(Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Point Editing) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the generating application should not allow shape grouping for the
Shape Grouping) corresponding connection shape. That is it cannot be combined within other shapes to
form a group of shapes. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the generating application should not allow position changes for the
Shape Movement) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the generating application should not allow size changes for the
Shape Resize) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noRot (Disallow Specifies that the generating application should not allow shape rotation changes for the
Shape Rotation) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the generating application should not allow selecting of the corresponding
Shape Selection) connection shape. That means also that no picture, shapes or text attached to this
connection shape can be selected if this attribute has been specified. If this attribute is
not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ConnectorLocking) is located in
§A.4.1. end note]
2736 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2747 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.2.12 dgm (Diagram to Animate)
This element specifies a reference to a diagram that should be animated within a sequence of slide animations.
In addition to simply acting as a reference to a diagram there is also animation build steps defined.
Attributes Description
bldStep (Animation Specifies which step this part of the diagram should be built using. For instance the
Build Step) diagram can be built as one object meaning it is animated as a single graphic.
Alternatively the diagram can be animated, or built as separate pieces.
The possible values for this attribute are defined by the ST_DgmBuildStep simple type
(§20.1.10.20).
id (Identifier) Specifies the GUID of the shape for this build step in the animation.
The possible values for this attribute are defined by the ST_Guid simple type (§22.9.2.4).
[Note: The W3C XML Schema definition of this element’s content model (CT_AnimationDgmElement) is located
in §A.4.1. end note]
20.1.2.2.13 endCxn (Connection End)
This element specifies the ending connection that should be made by the corresponding connector shape. This
connects the end tail of the connector to the final destination shape.
Attributes Description
id (Identifier) Specifies the id of the shape to make the final connection to.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
idx (Index) Specifies the index into the connection site table of the final connection shape. That is
there are many connection sites on a shape and it shall be specified which connection
site the corresponding connector shape should connect to.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Connection) is located in §A.4.1.
end note]
20.1.2.2.14 ext (Extension)
This element specifies an extension that is used for future extensions to the current version of DrawingML. This
allows for the specifying of currently unknown elements in the future that is used for later versions of
generating applications.
©ISO/IEC 2016 – All rights reserved 2737\n\n--- Page 2748 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: This element is not intended to reintroduce transitional schema into the strict conformance class. end
note]
Attributes Description
uri (Uniform Specifies the URI, or uniform resource identifier that represents the data stored under
Resource Identifier) this tag. The URI is used to identify the correct 'server' that can process the contents of
this tag.
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OfficeArtExtension) is located in
§A.4.1. end note]
20.1.2.2.15 extLst (Extension List)
This element specifies the extension list within which all future extensions of element type ext is defined. The
extension list along with corresponding future extensions is used to extend the storage capabilities of the
DrawingML framework. This allows for various new types of data to be stored natively within the framework.
[Note: The W3C XML Schema definition of this element’s content model (CT_OfficeArtExtensionList) is located in
§A.4.1. end note]
20.1.2.2.16 graphic (Graphic Object)
This element specifies the existence of a single graphic object. Document authors should refer to this element
when they wish to persist a graphical object of some kind. The specification for this graphical object is provided
entirely by the document author and referenced within the graphicData child element.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObject) is located in
§A.4.1. end note]
20.1.2.2.17 graphicData (Graphic Object Data)
This element specifies the reference to a graphic object within the document. This graphic object is provided
entirely by the document authors who choose to persist this data within the document.
[Note: Depending on the kind of graphical object used not every generating application that supports the
OOXML framework has the ability to render the graphical object. end note]
[Note: This element is not intended to reintroduce transitional schema into the strict conformance class. end
note]
Attributes Description
uri (Uniform Specifies the URI, or uniform resource identifier that represents the data stored under
Resource Identifier) this tag. The URI is used to identify the correct 'server' that can process the contents of
2738 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2749 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
this tag.
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectData) is located in
§A.4.1. end note]
20.1.2.2.18 graphicFrame (Graphic Frame)
This element specifies the existence of a graphics frame. This frame contains a graphic that was generated by an
external source and needs a container in which to be displayed on the slide surface.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlGraphicalObjectFrame) is
located in §A.4.1. end note]
20.1.2.2.19 graphicFrameLocks (Graphic Frame Locks)
This element specifies all locking properties for a graphic frame. These properties inform the generating
application about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding graphic frame. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noDrilldown Specifies that the generating application should not allow selecting of objects within the
(Disallow Selection corresponding graphic frame but allow selecting of the graphic frame itself. If this
of Child Shapes) attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the generating application should not allow shape grouping for the
Shape Grouping) corresponding graphic frame. That is it cannot be combined within other shapes to form
a group of shapes. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the corresponding graphic frame cannot be moved. Objects that reside
Shape Movement) within the graphic frame can still be moved unless they also have been locked. If this
attribute is not specified, then a value of false is assumed.
©ISO/IEC 2016 – All rights reserved 2739\n\n--- Page 2750 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the generating application should not allow size changes for the
Shape Resize) corresponding graphic frame. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the generating application should not allow selecting of the corresponding
Shape Selection) picture. That means also that no picture, shapes or text attached to this picture can be
selected if this attribute has been specified. If this attribute is not specified, then a value
of false is assumed.
[Note: If this attribute is specified to be true then the graphic frame cannot be selected
and the objects within the graphic frame cannot be selected as well. That is the entire
graphic frame including all sub-parts are considered un-selectable. end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectFrameLocking) is
located in §A.4.1. end note]
20.1.2.2.20 grpSp (Group shape)
This element specifies a group shape that represents many shapes grouped together. This shape is to be treated
just as if it were a regular shape but instead of being described by a single geometry it is made up of all the
shape geometries encompassed within it. Within a group shape each of the shapes that make up the group are
specified just as they normally would. The idea behind grouping elements however is that a single transform can
apply to many shapes at the same time.
[Example: Consider the following group shape.
<p:grpSp>
<p:nvGrpSpPr>
<p:cNvPr id="10" name="Group 9"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
2740 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2751 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:grpSpPr>
<a:xfrm>
<a:off x="838200" y="990600"/>
<a:ext cx="2426208" cy="978408"/>
<a:chOff x="838200" y="990600"/>
<a:chExt cx="2426208" cy="978408"/>
</a:xfrm>
</p:grpSpPr>
<p:sp>
…
</p:sp>
<p:sp>
…
</p:sp>
<p:sp>
…
</p:sp>
</p:grpSp>
In the above example we see three shapes specified within a single group. These three shapes have their
position and sizes specified just as they normally would within the shape tree. The generating application should
apply the transformation after the bounding box for the group shape has been calculated. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlGroupShape) is located in
§A.4.1. end note]
20.1.2.2.21 grpSpLocks (Group Shape Locks)
This element specifies all locking properties for a connection shape. These properties inform the generating
application about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding connection shape. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the corresponding group shape cannot be grouped. That is it cannot be
Shape Grouping) combined within other shapes to form a group of shapes. If this attribute is not specified,
then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the corresponding graphic frame cannot be moved. Objects that reside
©ISO/IEC 2016 – All rights reserved 2741\n\n--- Page 2752 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Moving Shape) within the graphic frame can still be moved unless they also have been locked. If this
attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the corresponding group shape cannot be resized. If this attribute is not
Shape Resizing) specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noRot (Disallow Specifies that the corresponding group shape cannot be rotated Objects that reside
Shape Rotation) within the group can still be rotated unless they also have been locked. If this attribute is
not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the corresponding group shape cannot have any part of it be selected. That
Shape Selection) means that no picture, shapes or attached text can be selected either if this attribute has
been specified. If this attribute is not specified, then a value of false is assumed.
[Note: This property is inherited by sub-elements and thus all shapes within the group
shape cannot be selected when this attribute is set to a value of true. end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noUngrp (Disallow Specifies that the generating application should not show adjust handles for the
Shape Ungrouping) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupLocking) is located in §A.4.1.
end note]
20.1.2.2.22 grpSpPr (Visual Group Shape Properties)
This element specifies the properties that are to be common across all of the shapes within the corresponding
group. If there are any conflicting properties within the group shape properties and the individual shape
properties then the individual shape properties should take precedence.
Attributes Description
bwMode (Black and Specifies that the group shape should be rendered using only black and white coloring.
2742 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2753 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
White Mode) That is the coloring information for the group shape should be converted to either black
or white when rendering the corresponding shapes.
No gray is to be used in rendering this image, only stark black and stark white.
[Note: This does not mean that the group shapes themselves are stored with only black
and white color information. This attribute instead sets the rendering mode that the
shapes use when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShapeProperties) is located
in §A.4.1. end note]
20.1.2.2.23 hlinkHover (Hyperlink for Hover)
This element specifies the hyperlink information to be activated when the user's mouse is hovered over the
corresponding object. The operation of the hyperlink is to have the specified action be activated when the
mouse of the user hovers over the object. When this action is activated then additional attributes can be used to
specify other tasks that should be performed along with the action.
Attributes Description
action (Action Specifies an action that is to be taken when this hyperlink is activated. This can be used to
Setting) specify a slide to be navigated to or a script of code to be run.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
endSnd (End Specifies if the URL in question should stop all sounds that are playing when it is clicked.
Sounds)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
highlightClick Specifies if this attribute has already been used within this document. That is when a
(Highlight Click) hyperlink has already been visited that this attribute would be utilized so the generating
application can determine the color of this text. If this attribute is omitted, then a value
of 0 or false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
history (Add Specifies whether to add this URI to the history when navigating to it. This allows for the
Hyperlink to Page viewing of this presentation without the storing of history information on the viewing
History) machine. If this attribute is omitted, then a value of 1 or true is assumed.
©ISO/IEC 2016 – All rights reserved 2743\n\n--- Page 2754 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Drawing Object Specifies the relationship id that when looked up in this slides relationship file contains
Hyperlink Target) the target of this hyperlink. This attribute cannot be omitted.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
invalidUrl (Invalid Specifies the URL when it has been determined by the generating application that the
URL) URL is invalid. That is the generating application can still store the URL but it is known
that this URL is not correct.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
tgtFrame (Target Specifies the target frame that is to be used when opening this hyperlink. When the
Frame) hyperlink is activated this attribute is used to determine if a new window is launched for
viewing or if an existing one can be used. If this attribute is omitted, than a new window
is opened.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
tooltip (Hyperlink Specifies the tooltip that should be displayed when the hyperlink text is hovered over
Tooltip) with the mouse. If this attribute is omitted, than the hyperlink text itself can be
displayed.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Hyperlink) is located in §A.4.1. end
note]
20.1.2.2.24 ln (Outline)
This element specifies an outline style that can be applied to a number of different objects such as shapes and
text. The line allows for the specifying of many different types of outlines including even line dashes and bevels.
Attributes Description
algn (Stroke Specifies the alignment to be used for the underline stroke.
Alignment)
The possible values for this attribute are defined by the ST_PenAlignment simple type
(§20.1.10.39).
2744 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2755 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
cap (Line Ending Specifies the ending caps that should be used for this line. [Note: Examples of cap types
Cap Type) are rounded, flat, etc. end note] If this attribute is omitted, than a value of square is
assumed.
The possible values for this attribute are defined by the ST_LineCap simple type
(§20.1.10.31).
cmpd (Compound Specifies the compound line type to be used for the underline stroke. If this attribute is
Line Type) omitted, then a value of sng is assumed.
The possible values for this attribute are defined by the ST_CompoundLine simple type
(§20.1.10.15).
w (Line Width) Specifies the width to be used for the underline stroke. If this attribute is omitted, then a
value of 0 is assumed.
The possible values for this attribute are defined by the ST_LineWidth simple type
(§20.1.10.35).
[Note: The W3C XML Schema definition of this element’s content model (CT_LineProperties) is located in §A.4.1.
end note]
20.1.2.2.25 nvCxnSpPr (Non-Visual Properties for a Connection Shape)
This element specifies all non-visual properties for a connection shape. This element is a container for the non-
visual identification properties, shape properties and application properties that are to be associated with a
connection shape. This allows for additional information that does not affect the appearance of the connection
shape to be stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlConnectorNonVisual) is
located in §A.4.1. end note]
20.1.2.2.26 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame)
This element specifies all non-visual properties for a graphic frame. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a graphic
frame. This allows for additional information that does not affect the appearance of the graphic frame to be
stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlGraphicFrameNonVisual) is
located in §A.4.1. end note]
20.1.2.2.27 nvGrpSpPr (Non-Visual Properties for a Group Shape)
This element specifies all non-visual properties for a group shape. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a group
©ISO/IEC 2016 – All rights reserved 2745\n\n--- Page 2756 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
shape. This allows for additional information that does not affect the appearance of the group shape to be
stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlGroupShapeNonVisual) is
located in §A.4.1. end note]
20.1.2.2.28 nvPicPr (Non-Visual Properties for a Picture)
This element specifies all non-visual properties for a picture. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a picture.
This allows for additional information that does not affect the appearance of the picture to be stored.
[Example: Consider the following PresentationML.
<p:pic>
…
<p:nvPicPr>
…
</p:nvPicPr>
…
</p:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlPictureNonVisual) is located in
§A.4.1. end note]
20.1.2.2.29 nvSpPr (Non-Visual Properties for a Shape)
This element specifies all non-visual properties for a shape. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a shape.
This allows for additional information that does not affect the appearance of the shape to be stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlShapeNonVisual) is located in
§A.4.1. end note]
20.1.2.2.30 pic (Picture)
This element specifies the existence of a picture object within the document.
[Example: Consider the following PresentationML that specifies the existence of a picture within a document.
This picture can have non-visual properties, a picture fill as well as shape properties attached to it.
2746 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2757 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:pic>
<p:nvPicPr>
<p:cNvPr id="4" name="lake.JPG" descr="Picture of a Lake" />
<p:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</p:cNvPicPr>
<p:nvPr/>
</p:nvPicPr>
<p:blipFill>
…
</p:blipFill>
<p:spPr>
…
</p:spPr>
</p:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlPicture) is located in §A.4.1.
end note]
20.1.2.2.31 picLocks (Picture Locks)
This element specifies all locking properties for a graphic frame. These properties inform the generating
application about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noAdjustHandles Specifies that the generating application should not show adjust handles for the
(Disallow Showing corresponding connection shape. If this attribute is not specified, then a value of false is
Adjust Handles) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeArrowhe Specifies that the generating application should not allow arrowhead changes for the
ads (Disallow corresponding connection shape. If this attribute is not specified, then a value of false is
Arrowhead assumed.
Changes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding connection shape. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
©ISO/IEC 2016 – All rights reserved 2747\n\n--- Page 2758 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
noChangeShapeTy Specifies that the generating application should not allow shape type changes for the
pe (Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Type Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noCrop (Disallow Specifies that the generating application should not allow cropping for the corresponding
Crop Changes) picture. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noEditPoints Specifies that the generating application should not allow shape point changes for the
(Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Point Editing) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the generating application should not allow shape grouping for the
Shape Grouping) corresponding connection shape. That is it cannot be combined within other shapes to
form a group of shapes. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the generating application should not allow position changes for the
Shape Movement) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the generating application should not allow size changes for the
Shape Resize) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noRot (Disallow Specifies that the generating application should not allow shape rotation changes for the
Shape Rotation) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the generating application should not allow selecting of the corresponding
Shape Selection) connection shape. That means also that no picture, shapes or text attached to this
connection shape can be selected if this attribute has been specified. If this attribute is
2748 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2759 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_PictureLocking) is located in §A.4.1.
end note]
20.1.2.2.32 snd (Hyperlink Sound)
This element specifies a sound to be played when a hyperlink within the document is activated. This sound is
specified from within the parent hyperlink element.
Attributes Description
embed (Embedded Specifies the identification information for an embedded audio file. This attribute is used
Audio File to specify the location of an object that resides locally within the file. [Note: A list of
Relationship ID) suggested audio types is provided in §15.2.2. end note]
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
name (Sound Specifies the original name or given short name for the corresponding sound. This is used
Name) to distinguish this sound from others by providing a human readable name for the
attached sound should the user need to identify the sound among others within the UI.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedWAVAudioFile) is
located in §A.4.1. end note]
20.1.2.2.33 sp (Shape)
This element specifies the existence of a single shape. A shape can either be a preset or a custom geometry,
defined using the DrawingML framework. In addition to a geometry each shape can have both visual and non-
visual properties attached. Text and corresponding styling information can also be attached to a shape. This
shape is specified along with all other shapes within either the shape tree or group shape elements.
[Note: Shapes are the preferred mechanism for specifying text on a slide. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlShape) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2749\n\n--- Page 2760 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.2.34 spLocks (Shape Locks)
This element specifies all locking properties for a shape. These properties inform the generating application
about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noAdjustHandles Specifies that the generating application should not show adjust handles for the
(Disallow Showing corresponding connection shape. If this attribute is not specified, then a value of false is
Adjust Handles) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeArrowhe Specifies that the generating application should not allow arrowhead changes for the
ads (Disallow corresponding connection shape. If this attribute is not specified, then a value of false is
Arrowhead assumed.
Changes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding connection shape. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeShapeTy Specifies that the generating application should not allow shape type changes for the
pe (Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Type Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noEditPoints Specifies that the generating application should not allow shape point changes for the
(Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Point Editing) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the generating application should not allow shape grouping for the
Shape Grouping) corresponding connection shape. That is it cannot be combined within other shapes to
form a group of shapes. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the generating application should not allow position changes for the
Shape Movement) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
2750 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2761 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the generating application should not allow size changes for the
Shape Resize) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noRot (Disallow Specifies that the generating application should not allow shape rotation changes for the
Shape Rotation) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the generating application should not allow selecting of the corresponding
Shape Selection) connection shape. That means also that no picture, shapes or text attached to this
connection shape can be selected if this attribute has been specified. If this attribute is
not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noTextEdit Specifies that the generating application should not allow editing of the shape text for
(Disallow Shape the corresponding shape. If this attribute is not specified, then a value of false is
Text Editing) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeLocking) is located in §A.4.1.
end note]
20.1.2.2.35 spPr (Shape Properties)
This element specifies the visual shape properties that can be applied to a shape.
Attributes Description
bwMode (Black and Specifies that the picture should be rendered using only black and white coloring. That is
White Mode) the coloring information for the picture should be converted to either black or white
when rendering the picture.
No gray is to be used in rendering this image, only stark black and stark white.
©ISO/IEC 2016 – All rights reserved 2751\n\n--- Page 2762 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Note: This does not mean that the picture itself that is stored within the file is
necessarily a black and white picture. This attribute instead sets the rendering mode that
the picture has applied to when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeProperties) is located in
§A.4.1. end note]
20.1.2.2.36 stCxn (Connection Start)
This element specifies the starting connection that should be made by the corresponding connector shape. This
connects the head of the connector to the first shape.
Attributes Description
id (Identifier) Specifies the id of the shape to make the final connection to.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
idx (Index) Specifies the index into the connection site table of the final connection shape. That is
there are many connection sites on a shape and it shall be specified which connection
site the corresponding connector shape should connect to.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Connection) is located in §A.4.1.
end note]
20.1.2.2.37 style (Shape Style)
This element specifies the style information for a shape.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeStyle) is located in §A.4.1.
end note]
20.1.2.2.38 sx (Horizontal Ratio)
This element specifies the horizontal ratio for use within a scaling calculation.
Attributes Description
d (Denominator) Specifies the denominator to be used within the equation.
2752 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2763 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema long datatype.
n (Numerator) Specifies the numerator to be used within the equation.
The possible values for this attribute are defined by the W3C XML Schema long datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Ratio) is located in §A.4.1. end
note]
20.1.2.2.39 sy (Vertical Ratio)
This element specifies the vertical ratio for use within a scaling calculation.
Attributes Description
d (Denominator) Specifies the denominator to be used within the equation.
The possible values for this attribute are defined by the W3C XML Schema long datatype.
n (Numerator) Specifies the numerator to be used within the equation.
The possible values for this attribute are defined by the W3C XML Schema long datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Ratio) is located in §A.4.1. end
note]
20.1.2.2.40 txBody (Shape Text Body)
This element specifies the existence of text to be contained within the corresponding shape. All visible text and
visible text related properties are contained within this element. There can be multiple paragraphs and within
paragraphs multiple runs of text.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextBody) is located in §A.4.1. end
note]
20.1.2.2.41 txSp (Text Shape)
This element specifies the existence of a text shape within a parent shape. This text shape is specifically used for
displaying text as it has only text related child elements.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlTextShape) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2753\n\n--- Page 2764 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.2.42 useSpRect (Use Shape Text Rectangle)
This element specifies that the text rectangle from the parent shape should be used for this text shape. If this
attribute is specified then the text rectangle, or text bounding box as it is also called should have the same
dimensions as the text bounding box of the parent shape within which this text shape resides.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlUseShapeRectangle) is located
in §A.4.1. end note]
20.1.2.2.43 cpLocks (Content Part Locks)
This element specifies all locking properties for a content part. These properties inform the generating
application about specific properties that have been previously locked and thus should not be changed.
Attributes Description
noAdjustHandles Specifies that the generating application should not show adjust handles for the
(Disallow Showing corresponding connection shape. If this attribute is not specified, then a value of false is
Adjust Handles) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeArrowhe Specifies that the generating application should not allow arrowhead changes for the
ads (Disallow corresponding connection shape. If this attribute is not specified, then a value of false is
Arrowhead assumed.
Changes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeAspect Specifies that the generating application should not allow aspect ratio changes for the
(Disallow Aspect corresponding connection shape. If this attribute is not specified, then a value of false is
Ratio Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noChangeShapeTy Specifies that the generating application should not allow shape type changes for the
pe (Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Type Change) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noEditPoints Specifies that the generating application should not allow shape point changes for the
(Disallow Shape corresponding connection shape. If this attribute is not specified, then a value of false is
Point Editing) assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noGrp (Disallow Specifies that the generating application should not allow shape grouping for the
2754 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2765 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Shape Grouping) corresponding connection shape. That is it cannot be combined within other shapes to
form a group of shapes. If this attribute is not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noMove (Disallow Specifies that the generating application should not allow position changes for the
Shape Movement) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noResize (Disallow Specifies that the generating application should not allow size changes for the
Shape Resize) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noRot (Disallow Specifies that the generating application should not allow shape rotation changes for the
Shape Rotation) corresponding connection shape. If this attribute is not specified, then a value of false is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
noSelect (Disallow Specifies that the generating application should not allow selecting of the corresponding
Shape Selection) connection shape. That means also that no picture, shapes, or text attached to this
connection shape can be selected if this attribute has been specified. If this attribute is
not specified, then a value of false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ContentPartLocking) is located in
§A.4.1. end note]
20.1.2.3 Colors
Given its own section within DrawingML Basics, colors are an integral part of the DrawingML framework.
Colors are used in virtually every object to help describe it's appearance when it is rendered on the screen. Since
not every generating application wishes to represent color in the same manner, it is possible to specify color in a
number of different ways.
20.1.2.3.1 alpha (Alpha)
This element specifies its input color with the specific opacity, but with its color unchanged.
©ISO/IEC 2016 – All rights reserved 2755\n\n--- Page 2766 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
val (Value) Specifies the opacity as expressed by a percentage value.
[Example: The following represents a green solid fill which is 50% opaque
<a:solidFill>
<a:srgbClr val="00FF00">
<a:alpha val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveFixedPercentage) is located
in §A.4.1. end note]
20.1.2.3.2 alphaMod (Alpha Modulation)
This element specifies a more or less opaque version of its input color. An alpha modulate never increases the
alpha beyond 100%. A 200% alpha modulate makes an input color twice as opaque as before. A 50% alpha
modulate makes an input color half as opaque as before.
Attributes Description
val (Value) Specifies the opacity as expressed by a percentage relative to the input color.
[Example: The following represents a green solid fill which is 50% opaque
<a:solidFill>
<a:srgbClr val="00FF00">
<a:alphaMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositivePercentage) is located in
§A.4.1. end note]
2756 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2767 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.3 alphaOff (Alpha Offset)
This element specifies a more or less opaque version of its input color. Increases or decreases the input alpha
percentage by the specified percentage offset. A 10% alpha offset increases a 50% opacity to 60%. A -10% alpha
offset decreases a 50% opacity to 40%. The transformed alpha values are limited to a range of 0 to 100%. A 10%
alpha offset increase to a 100% opaque object still results in 100% opacity.
Attributes Description
val (Value) Specifies the opacity as expressed by a percentage offset increase or decrease to the
input color. Increases never increase the opacity beyond 100%, decreases never decrease
the opacity below 0%.
[Example: The following represents a green solid fill which is 90% opaque
<a:solidFill>
<a:srgbClr val="00FF00">
<a:alphaOff val="-10%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_FixedPercentage) is located in
§A.4.1. end note]
20.1.2.3.4 blue (Blue)
This element specifies the input color with the specific blue component, but with the red and green color
components unchanged.
Attributes Description
val (Value) Specifies the value of the blue component. The assigned value is specified as a
percentage with 0% indicating minimal blue and 100% indicating maximum blue.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, FF, FF)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:blue val="100%"/>
</a:srgbClr>
</a:solidFill>
©ISO/IEC 2016 – All rights reserved 2757\n\n--- Page 2768 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.5 blueMod (Blue Modulation)
This element specifies the input color with its blue component modulated by the given percentage. A 50% blue
modulate reduces the blue component by half. A 200% blue modulate doubles the blue component.
Attributes Description
val (Value) Specifies the blue component as expressed by a percentage relative to the input color
component. Increases never increase the blue component beyond 100%, decreases
never decrease the blue component below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, 00, FF)
to value RRGGBB= (00, 00, 80)
<a:solidFill>
<a:srgbClr val="0000FF">
<a:blueMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.6 blueOff (Blue Offset)
This element specifies the input color with its blue component shifted, but with its red and green color
components unchanged.
Attributes Description
val (Value) Specifies the blue component as expressed by a percentage offset increase or decrease
to the input color component. Increases never increase the blue component
beyond 100%, decreases never decrease the blue component below 0%.
2758 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2769 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, 00, FF)
to value RRGGBB= (00, 00, CC)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:blueOff val="-20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.7 comp (Complement)
This element specifies that the color rendered should be the complement of its input color with the complement
being defined as such. Two colors are called complementary if, when mixed they produce a shade of grey. For
instance, the complement of red which is RGB (255, 0, 0) is cyan which is RGB (0, 255, 255).
Primary colors and secondary colors are typically paired in this way:
 red and cyan (where cyan is the mixture of green and blue)
 green and magenta (where magenta is the mixture of red and blue)
 blue and yellow (where yellow is the mixture of red and green)
[Example:
The following represents the complement of red:
<a:solidFill>
<a:srgbClr val="FF0000">
<a:comp/>
</a:srgbClr>
</a:solidFill>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ComplementTransform) is located
in §A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2759\n\n--- Page 2770 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.8 gamma (Gamma)
This element specifies that the output color rendered by the generating application should be the sRGB gamma
shift of the input color.
[Note: The W3C XML Schema definition of this element’s content model (CT_GammaTransform) is located in
§A.4.1. end note]
20.1.2.3.9 gray (Gray)
This element specifies a grayscale of its input color, taking into relative intensities of the red, green, and blue
primaries.
[Note: The W3C XML Schema definition of this element’s content model (CT_GrayscaleTransform) is located in
§A.4.1. end note]
20.1.2.3.10 green (Green)
This elements specifies the input color with the specified green component, but with its red and blue color
components unchanged.
Attributes Description
val (Value) Specifies the value of the green component. The assigned value is specified as a
percentage with 0% indicating minimal green and 100% indicating maximum green.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, 00, FF)
to value RRGGBB= (00, FF, FF)
<a:solidFill>
<a:srgbClr val="0000FF">
<a:green val="100%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.11 greenMod (Green Modulation)
This element specifies the input color with its green component modulated by the given percentage. A 50%
green modulate reduces the green component by half. A 200% green modulate doubles the green component.
2760 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2771 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
val (Value) Specifies the green component as expressed by a percentage relative to the input color
component. Increases never increase the green component beyond 100%, decreases
never decrease the green component below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, 80, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:greenMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.12 greenOff (Green Offset)
This element specifies the input color with its green component shifted, but with its red and blue color
components unchanged.
Attributes Description
val (Value) Specifies the green component as expressed by a percentage offset increase or decrease
to the input color component. Increases never increase the green component
beyond 100%, decreases never decrease the green component below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, CC, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:greenOff val="-20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
©ISO/IEC 2016 – All rights reserved 2761\n\n--- Page 2772 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.13 hslClr (Hue, Saturation, Luminance Color Model)
This element specifies a color using the HSL color model. A perceptual gamma of 2.2 is assumed.
Hue refers to the dominant wavelength of color, saturation refers to the purity of its hue, and luminance refers
to its lightness or darkness.
As with all colors, colors defined with the HSL color model can have color transforms applied to it.
[Example:
The color blue having RGB value RRGGBB = (00, 00, 80) is equivalent to
<a:solidFill>
<a:hslClr hue="14400000" sat="100%" lum="50%">
</a:solidFill>
end example]
Attributes Description
hue (Hue) Specifies the angular value describing the wavelength.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
lum (Luminance) Specifies the luminance referring to the lightness or darkness of the color. Expressed as a
percentage with 0% referring to maximal dark (black) and 100% referring to maximal
white.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
sat (Saturation) Specifies the saturation referring to the purity of the hue. Expressed as a percentage with
0% referring to grey, 100% referring to the purest form of the hue.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_HslColor) is located in §A.4.1. end
note]
20.1.2.3.14 hue (Hue)
This element specifies the input color with the specified hue, but with its saturation and luminance unchanged.
[Example: The following two solid fills are equivalent.
2762 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2773 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:solidFill>
<a:hslClr hue="14400000" sat="100%" lum="50%">
</a:solidFill>
<a:solidFill>
<a:hslClr hue="0" sat="100%" lum="50%">
<a:hue val="14400000"/>
<a:hslClr/>
</a:solidFill>
end example]
Attributes Description
val (Value) Specifies the actual angle value to be used with the input color's hue component.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveFixedAngle) is located in
§A.4.1. end note]
20.1.2.3.15 hueMod (Hue Modulate)
This element specifies the input color with its hue modulated by the given percentage. A 50% hue modulate
decreases the angular hue value by half. A 200% hue modulate doubles the angular hue value.
Attributes Description
val (Value) Specifies the hue as expressed by a percentage relative to the input color.
[Example: The following manipulates the fill color from having RGB value RRGGBB = (00,
FF, 00) to value RRGGBB = (FF, FF, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:hueMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositivePercentage) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2763\n\n--- Page 2774 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.16 hueOff (Hue Offset)
This element specifies the input color with its hue shifted, but with its saturation and luminance unchanged.
Attributes Description
val (Value) Specifies the actual angular value of the shift. The result of the shift shall be between 0
and 360 degrees. Shifts resulting in angular values less than 0 are treated as 0. Shifts
resulting in angular values greater than 360 are treated as 360.
[Example:
The following increases the hue angular value by 10 degrees.
<a:solidFill>
<a:hslClr hue="0" sat="100%" lum="50%"/>
<a:hueOff val="600000"/>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_Angle) is located in §A.4.1. end
note]
20.1.2.3.17 inv (Inverse)
This element specifies the inverse of its input color.
[Example:
The inverse of red (1, 0, 0) is cyan (0, 1, 1 ).
The following represents cyan, the inverse of red:
<a:solidFill>
<a:srgbClr val="FF0000">
<a:inv/>
</a:srgbClr>
</a:solidFill>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_InverseTransform) is located in
§A.4.1. end note]
2764 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2775 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.18 invGamma (Inverse Gamma)
This element specifies that the output color rendered by the generating application should be the inverse sRGB
gamma shift of the input color.
[Note: The W3C XML Schema definition of this element’s content model (CT_InverseGammaTransform) is
located in §A.4.1. end note]
20.1.2.3.19 lum (Luminance)
This element specifies the input color with the specified luminance, but with its hue and saturation unchanged.
Typically luminance values fall in the range [0%, 100%].
[Example:
The following two solid fills are equivalent:
<a:solidFill>
<a:hslClr hue="14400000" sat="100%" lum="50%">
</a:solidFill>
<a:solidFill>
<a:hslClr hue="14400000" sat="100%" lum="0%">
<a:lum val="50%"/>
<a:hslClr/>
</a:solidFill>
end example]
Attributes Description
val (Value) Specifies the value of the luminance. The assigned value is specified as a percentage with
0% indicating minimal luminance and 100% indicating maximum luminance.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, 66, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:lum val="20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
©ISO/IEC 2016 – All rights reserved 2765\n\n--- Page 2776 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.20 lumMod (Luminance Modulation)
This element specifies the input color with its luminance modulated by the given percentage. A 50% luminance
modulate reduces the luminance by half. A 200% luminance modulate doubles the luminance.
Attributes Description
val (Value) Specifies the luminance as expressed by a percentage relative to the input color.
Increases never increase the luminance beyond 100%, decreases never decrease the
luminance below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, 75, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:lumMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.21 lumOff (Luminance Offset)
This element specifies the input color with its luminance shifted, but with its hue and saturation unchanged.
Attributes Description
val (Value) Specifies the luminance as expressed by a percentage offset increase or decrease to the
input color. Increases never increase the luminance beyond 100%, decreases never
decrease the luminance below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, 99, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:lumOff val="-20%"/>
</a:srgbClr>
</a:solidFill>
2766 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2777 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.22 prstClr (Preset Color)
This element specifies a color which is bound to one of a predefined collection of colors.
[Example:
The following defines a solid fill bound to the "black" preset color.
<a:solidFill>
<a:prstClr val="black">
</a:solidFill>
end example]
Attributes Description
val (Value) Specifies the actual preset color value.
The possible values for this attribute are defined by the ST_PresetColorVal simple type
(§20.1.10.48).
[Note: The W3C XML Schema definition of this element’s content model (CT_PresetColor) is located in §A.4.1.
end note]
20.1.2.3.23 red (Red)
This element specifies the input color with the specified red component, but with its green and blue color
components unchanged.
Attributes Description
val (Value) Specifies the value of the red component. The assigned value is specified as a percentage
with 0% indicating minimal red and 100% indicating maximum red.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (FF, FF, 00)
©ISO/IEC 2016 – All rights reserved 2767\n\n--- Page 2778 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<a:solidFill>
<a:srgbClr val="00FF00">
<a:red val="100%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.24 redMod (Red Modulation)
This element specifies the input color with its red component modulated by the given percentage. A 50% red
modulate reduces the red component by half. A 200% red modulate doubles the red component.
Attributes Description
val (Value) Specifies the red component as expressed by a percentage relative to the input color
component. Increases never increase the red component beyond 100%, decreases never
decrease the red component below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (FF, 00, 00)
to value RRGGBB= (80, 00, 00)
<a:solidFill>
<a:srgbClr val="FF0000">
<a:redMod val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.25 redOff (Red Offset)
This element specifies the input color with its red component shifted, but with its green and blue color
components unchanged.
2768 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2779 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
val (Value) Specifies the red component as expressed by a percentage offset increase or decrease to
the input color component. Increases never increase the red component beyond 100%,
decreases never decrease the red component below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (FF, 00, 00)
to value RRGGBB= (CC, 00, 00)
<a:solidFill>
<a:srgbClr val="FF0000">
<a:redOff val="-20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.26 sat (Saturation)
This element specifies the input color with the specified saturation, but with its hue and luminance unchanged.
Typically saturation values fall in the range [0%, 100%].
[Example:
The following two solid fills are equivalent:
<a:solidFill>
<a:hslClr hue="14400000" sat="100%" lum="50%">
</a:solidFill>
<a:solidFill>
<a:hslClr hue="14400000" sat="0%" lum="50%">
<a:sat val="100000"/>
<a:hslClr/>
</a:solidFill>
end example]
Attributes Description
val (Value) Specifies the value of the saturation. The assigned value is specified as a percentage with
0% indicating minimal saturation and 100% indicating maximum saturation.
©ISO/IEC 2016 – All rights reserved 2769\n\n--- Page 2780 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (40, C0, 40)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:sat val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.27 satMod (Saturation Modulation)
This element specifies the input color with its saturation modulated by the given percentage. A 50% saturation
modulate reduces the saturation by half. A 200% saturation modulate doubles the saturation.
Attributes Description
val (Value) Specifies the saturation as expressed by a percentage relative to the input color.
Increases never increase the saturation beyond 100%, decreases never decrease the
saturation below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (66, 99, 66)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:satMod val="20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
2770 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2781 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.28 satOff (Saturation Offset)
This element specifies the input color with its saturation shifted, but with its hue and luminance unchanged. A
10% offset to 20% saturation yields 30% saturation.
Attributes Description
val (Value) Specifies the saturation as expressed by a percentage offset increase or decrease to the
input color. Increases never increase the saturation beyond 100%, decreases never
decrease the saturation below 0%.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (19, E5, 19)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:satOff val="-20%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_Percentage) is located in §A.4.1.
end note]
20.1.2.3.29 schemeClr (Scheme Color)
This element specifies a color bound to a user's theme. As with all elements which define a color, it is possible to
apply a list of color transforms to the base color defined.
Attributes Description
val (Value) Specifies the desired scheme.
[Example: The following represents a color bound to the "lt1" theme color
<a:solidFill>
<a:schemeClr val="lt1"/>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_SchemeColorVal simple type
(§20.1.10.54).
©ISO/IEC 2016 – All rights reserved 2771\n\n--- Page 2782 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_SchemeColor) is located in §A.4.1.
end note]
20.1.2.3.30 scrgbClr (RGB Color Model - Percentage Variant)
This element specifies a color using the red, green, blue RGB color model. Each component, red, green, and blue
is expressed as a percentage from 0% to 100%. A linear gamma of 1.0 is assumed.
Specifies the level of red as expressed by a percentage offset increase or decrease relative to the input color.
[Example: The following represent the same color
<a:solidFill>
<a:scrgbClr r="50%" g="50%" b="50%"/>
</a:solidFill>
<a:solidFill>
<a:srgbClr val="BCBCBC"/>
</a:solidFill>
end example]
Attributes Description
b (Blue) Specifies the percentage of blue.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
g (Green) Specifies the percentage of green.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
r (Red) Specifies the percentage of red.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_ScRgbColor) is located in §A.4.1.
end note]
20.1.2.3.31 shade (Shade)
This element specifies a darker version of its input color. A 10% shade is 10% of the input color combined with
90% black.
Attributes Description
val (Value) Specifies the shade as expressed by a percentage value.
2772 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2783 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (00, BC, 00)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:shade val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveFixedPercentage) is located
in §A.4.1. end note]
20.1.2.3.32 srgbClr (RGB Color Model - Hex Variant)
This element specifies a color using the red, green, blue RGB color model. Red, green, and blue is expressed as
sequence of hex digits, RRGGBB. A perceptual gamma of 2.2 is used.
Specifies the level of red as expressed by a percentage offset increase or decrease relative to the input color.
[Example: The following represent the same color
<a:solidFill>
<a:scrgbClr r="50%" g="50%" b="50%"/>
</a:solidFill>
<a:solidFill>
<a:srgbClr val="BCBCBC"/>
</a:solidFill>
end example]
Attributes Description
val (Value) The actual color value. Expressed as a sequence of hex digits RRGGBB.
The possible values for this attribute are defined by the ST_HexColorRGB simple type
(§22.9.2.5).
[Note: The W3C XML Schema definition of this element’s content model (CT_SRgbColor) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 2773\n\n--- Page 2784 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.2.3.33 sysClr (System Color)
This element specifies a color bound to predefined operating system elements.
[Example: The following represents the default color used for displaying text in a window.
<a:solidFill>
<a:sysClr val="windowText"/>
</a:solidFill>
end example]
Attributes Description
lastClr (Last Color) Specifies the color value that was last computed by the generating application.
The possible values for this attribute are defined by the ST_HexColorRGB simple type
(§22.9.2.5).
val (Value) Specifies the system color value.
The possible values for this attribute are defined by the ST_SystemColorVal simple type
(§20.1.10.58).
[Note: The W3C XML Schema definition of this element’s content model (CT_SystemColor) is located in §A.4.1.
end note]
20.1.2.3.34 tint (Tint)
This element specifies a lighter version of its input color. A 10% tint is 10% of the input color combined with
90% white.
Attributes Description
val (Value) Specifies the tint as expressed by a percentage value.
[Example: The following manipulates the fill from having RGB value RRGGBB = (00, FF, 00)
to value RRGGBB= (BC, FF, BC)
<a:solidFill>
<a:srgbClr val="00FF00">
<a:tint val="50%"/>
</a:srgbClr>
</a:solidFill>
end example]
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
2774 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2785 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveFixedPercentage) is located
in §A.4.1. end note]
20.1.3 Audio and Video
The Audio and Video portion of the DrawingML framework deals with all media of these two kinds that can be
attached to objects within a document. Types of audio that can be represented within a file are CD audio,
QuickTime audio, and any other generic audio. When dealing with generic audio there is the option for
embedding it within the file and also linking it. The linking option is preferable if the size of the audio file is too
large and thus increases the size of the document by an undesirable amount. For video there are two kinds that
can be represented and that is either a QuickTime movie or any other generic movie. When dealing with generic
video there is only the option of linking to the media as video is too large to embed within a document.
20.1.3.1 audioCd (Audio from CD)
This element specifies the existence of Audio from a CD. This element is specified within the non-visual
properties of an object. The audio shall be attached to an object as this is how it is represented within the
document. The actual playing of the sound however is done within the timing node list that is specified under
the timing element.
[Example: Consider the following picture object that has an audio from a CD attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="7" name="Rectangle 6">
<a:hlinkClick r:id="" action="ppaction://media"/>
</p:cNvPr>
<p:cNvPicPr>
<a:picLocks noRot="1"/>
</p:cNvPicPr>
<p:nvPr>
<a:audioCd>
<a:st track="1"/>
<a:end track="3" time="65"/>
</a:audioCd>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
In the above example, we see that there is a single audioCD element attached to this picture. This picture is
placed within the document just as a normal picture or shape would be. The id of this picture, namely 7 in this
case, is used to refer to this audioCD element from within the timing node list. For this example we see that the
audio for this CD starts playing at the 0 second mark on the first track and ends on the 1 minute 5 second mark
of the third track. end example]
©ISO/IEC 2016 – All rights reserved 2775\n\n--- Page 2786 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_AudioCD) is located in §A.4.1. end
note]
20.1.3.2 audioFile (Audio from File)
This element specifies the existence of an audio file. This element is specified within the non-visual properties of
an object. The audio shall be attached to an object as this is how it is represented within the document. The
actual playing of the audio however is done within the timing node list that is specified under the timing
element.
[Example: Consider the following picture object that has an audio file attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="7" name="Rectangle 6">
<a:hlinkClick r:id="" action="ppaction://media"/>
</p:cNvPr>
<p:cNvPicPr>
<a:picLocks noRot="1"/>
</p:cNvPicPr>
<p:nvPr>
<a:audioFile r:link="rId1"/>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
In the above example, we see that there is a single audioFile element attached to this picture. This picture is
placed within the document just as a normal picture or shape would be. The id of this picture, namely 7 in this
case, is used to refer to this audioFile element from within the timing node list. The Linked relationship id is
used to retrieve the actual audio file for playback purposes. end example]
Attributes Description
contentType Specifies the content type for the external file that is referenced by this element. Content
(Content Type of types define a media type, a subtype, and an optional set of parameters, as defined in
Linked Audio File) Part 2. If a rendering application cannot process external content of the content type
specified, then the specified content can be ignored. [Note: A list of suggested audio
types is provided in §15.2.2. end note]
If this attribute is omitted, application should attempt to determine the content type by
reading the contents of the relationship’s target.
A producer that wants interoperability should use the following standard format:
 audio/mpeg ISO/IEC 11172-3
The possible values for this attribute are defined by the W3C XML Schema string
2776 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2787 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
datatype.
link (Linked Specifies the identification information for a linked object. This attribute is used to
Relationship ID) specify the location of an object that does not reside within this file.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_AudioFile) is located in §A.4.1. end
note]
20.1.3.3 end (Audio End Time)
This element specifies the end point for a CD Audio sound element. Encompassed within this element are the
time and track at which the sound should halt its playback. This element is used in conjunction with an Audio
Start Time element to specify the time span for an entire audioCD sound element.
[Example: Consider the following DrawingML.
<a:audioCd>
<a:st track="1" time="2"/>
<a:end track="3" time="65"/>
</a:audioCd>
In the above example, the audioCD sound element shown specifies for a portion of audio spanning from 2
seconds into the first track to 1 minute, 5 seconds into the third track. end example]
Attributes Description
time (Time) Specifies the time in seconds that the CD Audio should be stopped at. If this attribute is
omitted, then a value of 0 is assumed.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
track (Track) Specifies which track of the CD this Audio stops playing at. This attribute is required and
cannot be omitted.
The possible values for this attribute are defined by the W3C XML Schema unsignedByte
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_AudioCDTime) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2777\n\n--- Page 2788 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.3.4 quickTimeFile (QuickTime from File)
This element specifies the existence of a QuickTime file, as defined in the 2007-09-04 version of the QuickTime
File Format Specification: http://developer.apple.com/documentation/QuickTime/QTFF/qtff.pdf. [Note: For
more information on the QuickTime format: http://developer.apple.com/reference/QuickTime/. end note]. This
element is specified within the non-visual properties of an object. The QuickTime file shall be attached to an
object as this is how it is represented within the document. The actual playing of the QuickTime however is done
within the timing node list that is specified under the timing element.
[Example: Consider the following picture object that has a QuickTime file attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="7" name="Rectangle 6">
<a:hlinkClick r:id="" action="ppaction://media"/>
</p:cNvPr>
<p:cNvPicPr>
<a:picLocks noRot="1"/>
</p:cNvPicPr>
<p:nvPr>
<a:quickTimeFile r:link="rId1"/>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
In the above example, we see that there is a single quickTimeFile element attached to this picture. This picture
is placed within the document just as a normal picture or shape would be. The id of this picture, namely 7 in this
case, is used to refer to this quickTimeFile element from within the timing node list. The Linked relationship id
is used to retrieve the actual video file for playback purposes. end example]
Attributes Description
link (Linked Specifies the identification information for a linked object. This attribute is used to
Relationship ID) specify the location of an object that does not reside within this file.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_QuickTimeFile) is located in §A.4.1.
end note]
2778 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2789 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.3.5 st (Audio Start Time)
This element specifies the start point for a CD Audio sound element. Encompassed within this element are the
time and track at which the sound should begin its playback. This element is used in conjunction with an Audio
End Time element to specify the time span for an entire audioCD sound element.
[Example: Consider the following DrawingML.
<a:audioCd>
<a:st track="1" time="2"/>
<a:end track="3" time="65"/>
</a:audioCd>
In the above example, the audioCD sound element shown specifies for a portion of audio spanning from 2
seconds into the first track to 1 minute, 5 seconds into the third track. end example]
Attributes Description
time (Time) Specifies the time in seconds that the CD Audio should be started at. If this attribute is
omitted, then a value of 0 is assumed.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
track (Track) Specifies which track of the CD this Audio begins playing on. This attribute is required and
cannot be omitted.
The possible values for this attribute are defined by the W3C XML Schema unsignedByte
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_AudioCDTime) is located in §A.4.1.
end note]
20.1.3.6 videoFile (Video from File)
This element specifies the existence of a video file. This element is specified within the non-visual properties of
an object. The video shall be attached to an object as this is how it is represented within the document. The
actual playing of the video however is done within the timing node list that is specified under the timing
element.
[Example: Consider the following picture object that has a video attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="7" name="Rectangle 6">
<a:hlinkClick r:id="" action="ppaction://media"/>
</p:cNvPr>
©ISO/IEC 2016 – All rights reserved 2779\n\n--- Page 2790 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:cNvPicPr>
<a:picLocks noRot="1"/>
</p:cNvPicPr>
<p:nvPr>
<a:videoFile r:link="rId1"/>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
In the above example, we see that there is a single videoFile element attached to this picture. This picture is
placed within the document just as a normal picture or shape would be. The id of this picture, namely 7 in this
case, is used to refer to this videoFile element from within the timing node list. The Linked relationship id is
used to retrieve the actual video file for playback purposes. end example]
Attributes Description
contentType Specifies the content type for the external file that is referenced by this element. Content
(Content Type of types define a media type, a subtype, and an optional set of parameters, as defined in
Linked Video File) Part 2. If a rendering application cannot process external content of the content type
specified, then the specified content can be ignored. [Note: A list of suggested video
types is provided in §15.2.17. end note]
If this attribute is omitted, application should attempt to determine the content type by
reading the contents of the relationship’s target.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
link (Linked Specifies the identification information for a linked video file. This attribute is used to
Relationship ID) specify the location of an object that does not reside within this file.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_VideoFile) is located in §A.4.1. end
note]
20.1.3.7 wavAudioFile (Audio from WAV File)
This element specifies the existence of an audio WAV file. This element is specified within the non-visual
properties of an object. The audio shall be attached to an object as this is how it is represented within the
document. The actual playing of the audio however is done within the timing node list that is specified under the
timing element.
2780 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2791 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following picture object that has an audio WAV file attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="7" name="Rectangle 6">
<a:hlinkClick r:id="" action="ppaction://media"/>
</p:cNvPr>
<p:cNvPicPr>
<a:picLocks noRot="1"/>
</p:cNvPicPr>
<p:nvPr>
<a:wavAudioFile r:embed="rId2"/>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
In the above example, we see that there is a single wavAudioFile element attached to this picture. This picture
is placed within the document just as a normal picture or shape would be. The id of this picture, namely 7 in this
case, is used to refer to this wavAudioFile element from within the timing node list. The Embedded relationship
id is used to retrieve the actual audio file for playback purposes. end example]
[Note: This element is generally used for the purposes of embedding audio files within the document. For linking
to generic audio files the audioFile element should be used. end note]
Attributes Description
embed (Embedded Specifies the identification information for an embedded audio file. This attribute is used
Audio File to specify the location of an object that resides locally within the file. [Note: A list of
Relationship ID) suggested audio types is provided in §15.2.2. end note]
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
name (Sound Specifies the original name or given short name for the corresponding sound. This is used
Name) to distinguish this sound from others by providing a human readable name for the
attached sound should the user need to identify the sound among others within the UI.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedWAVAudioFile) is
located in §A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2781\n\n--- Page 2792 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4 Styles
Styles within DrawingML refer to the way a particular object (be it text or a shape, or anything else) is formatted.
Different aspects, ranging from color, line type, fill, and effects applied to the object can be predefined within a
theme. The main purpose of a theme is to define a style matrix from which a document can pull style
information from in order to format the visual look of objects in a document.
20.1.4.1 Styles
The elements in this section compose the basic definition of a style, including its associated colors, effect styles,
line styles, fill styles, background styles, and font scheme.
20.1.4.1.1 accent1 (Accent 1)
This element defines a color that happens to be the accent 1 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.2 accent2 (Accent 2)
This element defines a color that happens to be the accent 2 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
2782 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2793 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.3 accent3 (Accent 3)
This element defines a color that happens to be the accent 3 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 2783\n\n--- Page 2794 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.1.4 accent4 (Accent 4)
This element defines a color that happens to be the accent 4 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.5 accent5 (Accent 5)
This element defines a color that happens to be the accent 5 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
2784 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2795 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.6 accent6 (Accent 6)
This element defines a color that happens to be the accent 1 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.7 bgFillStyleLst (Background Fill Style List)
This element defines a list of background fills that are used within a theme. The background fills consist of three
fills, arranged in order from subtle to moderate to intense.
[Example: Consider the following example of a background fill style list within DrawingML:
©ISO/IEC 2016 – All rights reserved 2785\n\n--- Page 2796 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<bgFillStyleLst>
<solidFill>
…
</solidFill>
<gradFill rotWithShape="1">
…
</gradFill>
<blipFill>
…
</blipFill>
</bgFillStyleLst>
In this example, we see that the list contains a solid fill for the subtle fill, a gradient fill for the moderate fill and
an image fill for the intense background fill. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_BackgroundFillStyleList) is located
in §A.4.1. end note]
20.1.4.1.8 custClr (Custom color)
This element defines a custom color. The custom colors are used within a custom color list to define custom
colors that are extra colors that can be appended to a theme. This is useful within corporate scenarios where
there is a set corporate color palette from which to work.
Attributes Description
name (Name) The name of the color shown in the color picker.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomColor) is located in §A.4.1.
end note]
20.1.4.1.9 dk1 (Dark 1)
This element defines a color that happens to be the dark 1 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
2786 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2797 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.10 dk2 (Dark 2)
This element defines a color that happens to be the dark 2 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 2787\n\n--- Page 2798 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.1.11 effectStyle (Effect Style)
This element defines a set of effects and 3D properties that can be applied to an object.
[Example: Consider the following example of an effect style within DrawingML:
<effectStyle>
<effectLst>
<outerShdw blurRad="57150" dist="38100" dir="5400000" algn="ctr"
rotWithShape="0">
<schemeClr val="phClr">
<shade val="9000"/>
<satMod val="105000"/>
<alpha val="48000"/>
</schemeClr>
</outerShdw>
</effectLst>
</effectStyle>
In this example, an outer shadow is being applied to a shape as the moderate effect. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectStyleItem) is located in
§A.4.1. end note]
20.1.4.1.12 effectStyleLst (Effect Style List)
This element defines a set of three effect styles that create the effect style list for a theme. The effect styles are
arranged in order of subtle to moderate to intense.
[Example: Consider the following example of an effect style list within DrawingML:
<effectStyleLst>
<effectStyle>
<effectLst>
<outerShdw blurRad="57150" dist="38100" dir="5400000"
algn="ctr" rotWithShape="0">
…
</outerShdw>
</effectLst>
</effectStyle>
2788 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2799 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<effectStyle>
<effectLst>
<outerShdw blurRad="57150" dist="38100" dir="5400000"
algn="ctr" rotWithShape="0">
…
</outerShdw>
</effectLst>
</effectStyle>
<effectStyle>
<effectLst>
<outerShdw blurRad="57150" dist="38100" dir="5400000"
algn="ctr" rotWithShape="0">
…
</outerShdw>
</effectLst>
<scene3d>
…
</scene3d>
<sp3d prstMaterial="powder">
…
</sp3d>
</effectStyle>
</effectStyleLst>
In this example, we see three effect styles defined. The first two (subtle and moderate) define an outer shadow
as the effect, while the third effect style (intense) defines an outer shadow along with 3D properties which are
to be applied to the object as well. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectStyleList) is located in §A.4.1.
end note]
20.1.4.1.13 fillStyleLst (Fill Style List)
This element defines a set of three fill styles that are used within a theme. The three fill styles are arranged in
order from subtle to moderate to intense.
[Example: Consider the following example of a fill style list within DrawingML:
<fillStyleLst>
<solidFill>
…
</solidFill>
<gradFill rotWithShape="1">
…
</gradFill>
©ISO/IEC 2016 – All rights reserved 2789\n\n--- Page 2800 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<gradFill rotWithShape="1">
…
</gradFill>
</fillStyleLst>
In this example, we see three fill styles being defined within the fill style list. The first style is the subtle style and
defines simply a solid fill. The second and third styles (moderate and intense fills respectively) define gradient
fills. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_FillStyleList) is located in §A.4.1.
end note]
20.1.4.1.14 fmtScheme (Format Scheme)
This element contains the background fill styles, effect styles, fill styles, and line styles which define the style
matrix for a theme. The style matrix consists of subtle, moderate, and intense fills, lines, and effects. The
background fills are not generally thought of to directly be associated with the matrix, but do play a role in the
style of the overall document. Usually, a given object chooses a single line style, a single fill style, and a single
effect style in order to define the overall final look of the object.
[Example: Consider the following example of the style matrix in use within DrawingML:
In this example, we see a shape styled which utilizes different aspects from the above defined style matrix. end
example]
2790 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2801 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
name (Name) Defines the name for the format scheme. The name is simply a human readable string
which identifies the format scheme in the user interface.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_StyleMatrix) is located in §A.4.1.
end note]
20.1.4.1.15 folHlink (Followed Hyperlink)
This element defines a color that happens to be the followed hyperlink color. The set of twelve colors come
together to form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.16 font (Font)
This element defines a font within the styles area of DrawingML. A font is defined by a script along with a
typeface.
[Example: Consider the following example of a font in DrawingML:
<font script="Thai" typeface="Cordia New"/>
In this example, we see that the script 'Thai' is supposed to use the font face 'Cordia New'. end example]
©ISO/IEC 2016 – All rights reserved 2791\n\n--- Page 2802 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
script (Script) Specifies the script, or language, in which the typeface is supposed to be used.
[Note: It is recommended that script names as specified in ISO 15924 are used. end note]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
typeface (Typeface) Specifies the font face to use.
The possible values for this attribute are defined by the ST_TextTypeface simple type
(§20.1.10.81).
[Note: The W3C XML Schema definition of this element’s content model (CT_SupplementalFont) is located in
§A.4.1. end note]
20.1.4.1.17 fontRef (Font Reference)
This element represents a reference to a themed font. When used it specifies which themed font to use along
with a choice of color.
[Example: Consider the following example of a font reference within DrawingML:
<fontRef idx="minor">
<schemeClr val="tx1"/>
</fontRef>
In this example, we see a font referencing the minor font defined within the theme. end example]
Attributes Description
idx (Identifier) Specifies the identifier of the font to reference.
The possible values for this attribute are defined by the ST_FontCollectionIndex simple
type (§20.1.10.25).
[Note: The W3C XML Schema definition of this element’s content model (CT_FontReference) is located in §A.4.1.
end note]
20.1.4.1.18 fontScheme (Font Scheme)
This element defines the font scheme within the theme. The font scheme consists of a pair of major and minor
fonts for which to use in a document. The major font corresponds well with the heading areas of a document,
and the minor font corresponds well with the normal text or paragraph areas.
[Example: Consider the following example of a font scheme within DrawingML:
2792 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2803 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<fontScheme name="sample">
<majorFont>
…
</majorFont>
<minorFont>
…
</minorFont>
</fontScheme>
In this example, we see the major and minor font lists within the font scheme that is named 'sample'. end
example]
Attributes Description
name (Name) The name of the font scheme shown in the user interface.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_FontScheme) is located in §A.4.1.
end note]
20.1.4.1.19 hlink (Hyperlink)
This element defines a color that happens to be the hyperlink color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
©ISO/IEC 2016 – All rights reserved 2793\n\n--- Page 2804 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.20 lnDef (Line Default)
This element defines a default line that is used within a document.
[Example: Consider the following example of a default line defined in DrawingML:
<lnDef>
<spPr/>
<bodyPr/>
<lstStyle/>
<style>
<lnRef idx="1">
<schemeClr val="accent2"/>
</lnRef>
<fillRef idx="0">
<schemeClr val="accent2"/>
</fillRef>
<effectRef idx="0">
<schemeClr val="accent2"/>
</effectRef>
<fontRef idx="minor">
<schemeClr val="tx1"/>
</fontRef>
</style>
</lnDef>
In this example, we see that the default line for the document is being defined as a themed line which
references the subtle line style with idx equal to 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_DefaultShapeDefinition) is located
in §A.4.1. end note]
20.1.4.1.21 lnStyleLst (Line Style List)
This element defines a list of three line styles for use within a theme. The three line styles are arranged in order
from subtle to moderate to intense versions of lines. This list makes up part of the style matrix.
[Example: Consider the following example of a line style list within DrawingML:
2794 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2805 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<lnStyleLst>
<ln w="9525" cap="flat" cmpd="sng" algn="ctr">
<solidFill>
<schemeClr val="phClr">
<shade val="50000"/>
<satMod val="103000"/>
</schemeClr>
</solidFill>
<prstDash val="solid"/>
</ln>
<ln w="25400" cap="flat" cmpd="sng" algn="ctr">
<solidFill>
<schemeClr val="phClr"/>
</solidFill>
<prstDash val="solid"/>
</ln>
<ln w="38100" cap="flat" cmpd="sng" algn="ctr">
<solidFill>
<schemeClr val="phClr"/>
</solidFill>
<prstDash val="solid"/>
</ln>
</lnStyleLst>
In this example, we see three lines defined within a line style list. The first line corresponds to the subtle line,
the second to the moderate, and the third corresponds to the intense line defined in the theme. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_LineStyleList) is located in §A.4.1.
end note]
20.1.4.1.22 lt1 (Light 1)
This element defines a color that happens to be the accent 1 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
©ISO/IEC 2016 – All rights reserved 2795\n\n--- Page 2806 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.4.1.23 lt2 (Light 2)
This element defines a color that happens to be the accent 1 color. The set of twelve colors come together to
form the color scheme for a theme.
[Example: Consider the following example of a set of colors that form a color scheme:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
2796 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2807 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.1.24 majorFont (Major Font)
This element defines the set of major fonts which are to be used under different languages or locals.
[Example: Consider the following example of the major fonts being defined within DrawingML:
<majorFont>
<latin typeface="Calibri"/>
<ea typeface="Arial"/>
<cs typeface="Arial"/>
<font script="Jpan" typeface="ＭＳ Ｐゴシック"/>
<font script="Hang" typeface="HY중고딕"/>
<font script="Hans" typeface="隶书"/>
<font script="Hant" typeface="微軟正黑體"/>
<font script="Arab" typeface="Traditional Arabic"/>
<font script="Hebr" typeface="Arial"/>
<font script="Thai" typeface="Cordia New"/>
<font script="Ethi" typeface="Nyala"/>
<font script="Beng" typeface="Vrinda"/>
<font script="Gujr" typeface="Shruti"/>
<font script="Khmr" typeface="DaunPenh"/>
<font script="Knda" typeface="Tunga"/>
</majorFont>
In this example, we see the latin, east asian, and complex script fonts defined along with many fonts for
different locals. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_FontCollection) is located in §A.4.1.
end note]
20.1.4.1.25 minorFont (Minor fonts)
This element defines the set of minor fonts that are to be used under different languages or locals.
[Example: Consider the following example of the minor fonts being defined within DrawingML:
©ISO/IEC 2016 – All rights reserved 2797\n\n--- Page 2808 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<minorFont>
<latin typeface="Calibri"/>
<ea typeface="Arial"/>
<cs typeface="Arial"/>
<font script="Jpan" typeface="ＭＳ Ｐゴシック"/>
<font script="Hang" typeface="HY중고딕"/>
<font script="Hans" typeface="隶书"/>
<font script="Hant" typeface="微軟正黑體"/>
<font script="Arab" typeface="Traditional Arabic"/>
<font script="Hebr" typeface="Arial"/>
<font script="Thai" typeface="Cordia New"/>
<font script="Ethi" typeface="Nyala"/>
<font script="Beng" typeface="Vrinda"/>
<font script="Gujr" typeface="Shruti"/>
<font script="Khmr" typeface="DaunPenh"/>
<font script="Knda" typeface="Tunga"/>
</minorFont>
In this example, we see the latin, east asian, and complex script fonts defined along with many fonts for
different locals. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_FontCollection) is located in §A.4.1.
end note]
20.1.4.1.26 scene3d (3D Scene Properties)
This element defines optional scene-level 3D properties to apply to an object.
[Note: The W3C XML Schema definition of this element’s content model (CT_Scene3D) is located in §A.4.1. end
note]
20.1.4.1.27 spDef (Shape Default)
This element defines the formatting that is associated with the default shape. The default formatting can be
applied to a shape when it is initially inserted into a document.
[Example: Consider the following example of a shape default being used within DrawingML:
<spDef>
<spPr>
<solidFill>
<schemeClr val="accent2">
<shade val="75000"/>
</schemeClr>
</solidFill>
</spPr>
2798 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2809 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<bodyPr rtlCol="0" anchor="ctr"/>
<lstStyle>
<defPPr algn="ctr">
<defRPr/>
</defPPr>
</lstStyle>
<style>
<lnRef idx="1">
<schemeClr val="accent1"/>
</lnRef>
<fillRef idx="2">
<schemeClr val="accent1"/>
</fillRef>
<effectRef idx="1">
<schemeClr val="accent1"/>
</effectRef>
<fontRef idx="minor">
<schemeClr val="dk1"/>
</fontRef>
</style>
</spDef>
In this example, we see a default shape which references a certain themed fill, line, effect, and font along with
an override fill to these. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_DefaultShapeDefinition) is located
in §A.4.1. end note]
20.1.4.1.28 txDef (Text Default)
This element defines the default formatting which is applied to text in a document by default. The default
formatting can and should be applied to the shape when it is initially inserted into a document.
[Example: Consider the following example of a text default being used within DrawingML:
<txDef>
<spPr>
<solidFill>
<schemeClr val="accent2">
<shade val="75000"/>
</schemeClr>
</solidFill>
</spPr>
<bodyPr rtlCol="0" anchor="ctr"/>
©ISO/IEC 2016 – All rights reserved 2799\n\n--- Page 2810 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<lstStyle>
<defPPr algn="ctr">
<defRPr/>
</defPPr>
</lstStyle>
<style>
<lnRef idx="1">
<schemeClr val="accent1"/>
</lnRef>
<fillRef idx="2">
<schemeClr val="accent1"/>
</fillRef>
<effectRef idx="1">
<schemeClr val="accent1"/>
</effectRef>
<fontRef idx="minor">
<schemeClr val="dk1"/>
</fontRef>
</style>
</txDef>
In this example, we see a default text which references a certain themed fill, line, effect, and font along with an
override fill to these. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_DefaultShapeDefinition) is located
in §A.4.1. end note]
20.1.4.2 Table Styles
Table styles are responsible for the rapid formatting that can be applied to a table. This rapid formatting takes
different parts of a table into account, such as if the first row or last row should be emphasized, or if there is
some type of banding (row for example) present on the table. All of these different types of formatting can be
defined within a table style
20.1.4.2.1 band1H (Band 1 Horizontal)
This element describes the formatting for the first row in horizontal banding. Two different row formatting are
applied to the table alternating in order to create a banding effect on the table.
[Example: Consider the following example of band 1 horizontal being used within DrawingML:
2800 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2811 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<band1H>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1">
<tint val="40000"/>
</schemeClr>
</solidFill>
</fill>
</tcStyle>
</band1H>
In this example, we set the fill to be a solid fill referencing the accent 1 color defined in the theme. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.2 band1V (Band 1 Vertical)
This element describes the formatting for the first row in vertical banding. Two different column formattings
are applied to the table alternating in order to create a banding effect on the table.
[Example: Consider the following example of band 1 vertical being used within DrawingML:
<band1V>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1">
<tint val="40000"/>
</schemeClr>
</solidFill>
</fill>
</tcStyle>
</band1V>
©ISO/IEC 2016 – All rights reserved 2801\n\n--- Page 2812 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This markup example sets the fill to be a solid fill referencing the accent 1 color defined in the theme. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.3 band2H (Band 2 Horizontal)
This element describes the formatting for the second row in horizontal banding. Two different row formatting
are applied to the table alternating in order to create a banding effect on the table.
[Example: Consider the following example of band 2 horizontal being used within DrawingML:
<band2H>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent2">
<tint val="40000"/>
</schemeClr>
</solidFill>
</fill>
</tcStyle>
</band2H>
2802 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2813 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
In this example, we set the fill to be a solid fill referencing the accent 2 color defined in the theme. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.4 band2V (Band 2 Vertical)
This element describes the formatting for the second row in vertical banding. Two different row formatting are
applied to the table alternating in order to create a banding effect on the table.
[Example: Consider the following example of band 2 vertical being used within DrawingML:
<band2V>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent2">
<tint val="40000"/>
</schemeClr>
</solidFill>
</fill>
</tcStyle>
</band2V>
In this example, we set the fill to be a solid fill referencing the accent 2 color defined in the theme. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2803\n\n--- Page 2814 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.5 bevel (Bevel)
This element defines the properties of the bevel associated with the 3D effect applied to a cell in a table.
Attributes Description
h (Height) Specifies the height of the bevel, or how far above the shape it is applied.
[Example: Consider the following example bevel
In this example, we see the height of an example bevel on a shape. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
prst (Preset Bevel) Specifies the preset bevel type which defines the look of the bevel.
The possible values for this attribute are defined by the ST_BevelPresetType simple type
(§20.1.10.9).
w (Width) Specifies the width of the bevel, or how far into the shape it is applied.
[Example: Consider the following example bevel
In this example, we see the width of an example bevel on a shape. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_Bevel) is located in §A.4.1. end
note]
2804 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2815 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.6 bottom (Bottom Border)
This element defines the line properties associated with the bottom border in a table cell.
[Example: Consider the following example of the bottom border in use within DrawingML:
<bottom>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</bottom>
In this example, we see the bottom border on a table cell to be a single 1pt line which is colored accent 1. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.7 effect (Effect)
This element defines the effect that can be applied to a table as a whole through a table style.
[Example: Consider the following example of an effect in use within DrawingML:
<effect>
<effectLst>
<glow rad="228600">
<schemeClr val="accent1">
<satMod val="175000"/>
<alpha val="40000"/>
</schemeClr>
</glow>
</effectLst>
</effect>
In this example, we see a glow being defined within the table style that is applied to the table as a whole. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectProperties) is located in
§A.4.1. end note]
20.1.4.2.8 effectRef (Effect Reference)
This element defines a reference to an effect style within the style matrix. The idx attribute refers the index of
an effect style within the effectStyleLst element.
©ISO/IEC 2016 – All rights reserved 2805\n\n--- Page 2816 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
idx (Style Matrix Specifies the style matrix index of the style referred to.
Index)
The possible values for this attribute are defined by the ST_StyleMatrixColumnIndex
simple type (§20.1.10.57).
[Note: The W3C XML Schema definition of this element’s content model (CT_StyleMatrixReference) is located in
§A.4.1. end note]
20.1.4.2.9 fill (Fill)
This element defines the fill that is applied to the table as a whole. The background of the table can contain a
single fill that is the entire size of the table. This can allow for gradient fills, or image fills, which span the entire
size of the table.
[Example: Consider the following example of a fill on a table background in DrawingML:
<fill>
<gradFill flip="none" rotWithShape="1">
<gsLst>
<gs pos="0">
<schemeClr val="accent2">
<shade val="75000"/>
</schemeClr>
</gs>
<gs pos="100000">
<schemeClr val="accent2">
<shade val="75000"/>
<tint val="20000"/>
</schemeClr>
</gs>
</gsLst>
<lin ang="2700000" scaled="1"/>
<tileRect/>
</gradFill>
</fill>
In this example, we apply a gradient fill to the entire table on the background shape of the table. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_FillProperties) is located in §A.4.1.
end note]
2806 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2817 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.10 fillRef (Fill Reference)
This element defines a reference to a fill style within the style matrix. The idx attribute refers to the index of a
fill style or background fill style within the presentation's style matrix, defined by the fmtScheme element. A
value of 0 or 1000 indicates no background, values 1-999 refer to the index of a fill style within the fillStyleLst
element, and values 1001 and above refer to the index of a background fill style within the bgFillStyleLst
element. The value 1001 corresponds to the first background fill style, 1002 to the second background fill style,
and so on.
[Example:
<a:fillRef idx="2">
<a:schemeClr val="accent2"/>
</a:fillRef>
The above code indicates the object is to have the style's second fill style using the accent2 color of the color
scheme.
end example]
[Example:
<a:fillRef idx="1001">
<a:schemeClr val="accent2"/>
</a:fillRef>
The above code indicates the object is to have the style's first background fill style using the accent2 color of the
color scheme.
end example]
Attributes Description
idx (Style Matrix Specifies the style matrix index of the style referred to.
Index)
The possible values for this attribute are defined by the ST_StyleMatrixColumnIndex
simple type (§20.1.10.57).
[Note: The W3C XML Schema definition of this element’s content model (CT_StyleMatrixReference) is located in
§A.4.1. end note]
20.1.4.2.11 firstCol (First Column)
This element defines the cell formatting which can be applied to the first column of the table.
[Example: Consider the following example of first column formatting within DrawingML:
©ISO/IEC 2016 – All rights reserved 2807\n\n--- Page 2818 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<firstCol>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</firstCol>
In this example, we define the first column cell fills to be accent 1 along with the text properties to be bold when
first column formatting is enabled through the user interface. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.12 firstRow (First Row)
This element defines the cell formatting which can be applied to the first row of the table.
[Example: Consider the following example of first row formatting within DrawingML:
2808 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2819 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<firstRow>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</firstRow>
In this example, we define the first row cell fills to be accent 1 along with the text properties to be bold when
first row formatting is enabled through the user interface. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.13 font (Font)
This element defines the font to be used within a given table cell text style. This element allows for exact
definition of the font within the table style instead of referencing a themed font.
[Note: The W3C XML Schema definition of this element’s content model (CT_FontCollection) is located in §A.4.1.
end note]
20.1.4.2.14 insideH (Inside Horizontal Border)
This element defines the line properties associated with the inner horizontal borders in a table.
[Example: Consider the following example of the inner horizontal borders in use within DrawingML:
©ISO/IEC 2016 – All rights reserved 2809\n\n--- Page 2820 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<insideH>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</insideH>
In this example, we see the inner horizontal borders in a table to be a single 1pt line which is colored accent 1.
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.15 insideV (Inside Vertical Border)
This element defines the line properties associated with the inner vertical borders in a table.
[Example: Consider the following example of the inside vertical borders in use within DrawingML:
<insideV>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</insideV>
In this example, we see the inner vertical borders in a table to be a single 1pt line which is colored accent 1. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.16 lastCol (Last Column)
This element defines the cell formatting which can be applied to the last column of the table.
[Example: Consider the following example of last column formatting within DrawingML:
<lastCol>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
2810 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2821 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</lastCol>
In this example, we define the last column cell fills to be accent 1 along with the text properties to be bold when
last column formatting is enabled through the user interface. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.17 lastRow (Last Row)
This element defines the cell formatting which can be applied to the last row of the table.
[Example: Consider the following example of last row formatting within DrawingML:
<lastRow>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
©ISO/IEC 2016 – All rights reserved 2811\n\n--- Page 2822 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</lastRow>
In this example, we define the last row cell fills to be accent 1 along with the text properties to be bold when last
row formatting is enabled through the user interface. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.18 left (Left Border)
This element defines the line properties associated with the left border in a table cell.
[Example: Consider the following example of the left border in use within DrawingML:
<left>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</left>
In this example, we see the left border on a table cell to be a single 1pt line which is colored accent 1. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
2812 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2823 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.19 lnRef (Line Reference)
This element defines a reference to a line style within the style matrix. The idx attribute refers the index of a
line style within the fillStyleLst element.
Attributes Description
idx (Style Matrix Specifies the style matrix index of the style referred to.
Index)
The possible values for this attribute are defined by the ST_StyleMatrixColumnIndex
simple type (§20.1.10.57).
[Note: The W3C XML Schema definition of this element’s content model (CT_StyleMatrixReference) is located in
§A.4.1. end note]
20.1.4.2.20 neCell (Northeast Cell)
This element defies the formatting for the cell in the northeast corner of a table when both the first row
formatting and last column formatting are enabled. This formatting is only applied to the single cell which
overlaps between the two formatting options.
[Example: Consider the following example of the northeast cell formatting within DrawingML:
<neCell>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</neCell>
In this example, we specifically set the northeast cell to contain bold text with a solid cell fill in the color of
accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2813\n\n--- Page 2824 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.21 nwCell (Northwest Cell)
This element defies the formatting for the cell in the northwest corner of a table when both the first row
formatting and first column formatting are enabled. This formatting is only applied to the single cell which
overlaps between the two formatting options.
[Example: Consider the following example of the northwest cell formatting within DrawingML:
<nwCell>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</nwCell>
In this example, we specifically set the northwest cell to contain bold text with a solid cell fill in the color of
accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.22 right (Right Border)
This element defines the line properties associated with the right border in a table cell.
[Example: Consider the following example of the right border in use within DrawingML:
<right>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</right>
In this example, we see the right border on a table cell to be a single 1pt line which is colored accent 1. end
example]
2814 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2825 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.23 seCell (Southeast Cell)
This element defies the formatting for the cell in the southeast corner of a table when both the last row
formatting and last column formatting are enabled. This formatting is only applied to the single cell which
overlaps between the two formatting options.
[Example: Consider the following example of the southeast cell formatting within DrawingML:
<seCell>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</seCell>
In this example, we specifically set the southeast cell to contain bold text with a solid cell fill in the color of
accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.24 swCell (Southwest Cell)
This element defies the formatting for the cell in the southwest corner of a table when both the last row
formatting and first column formatting are enabled. This formatting is only applied to the single cell which
overlaps between the two formatting options.
[Example: Consider the following example of the southwest cell formatting within DrawingML:
©ISO/IEC 2016 – All rights reserved 2815\n\n--- Page 2826 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<swCell>
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
<tcStyle>
<tcBdr/>
<fill>
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</fill>
</tcStyle>
</swCell>
In this example, we specifically set the southwest cell to contain bold text with a solid cell fill in the color of
accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.4.2.25 tblBg (Table Background)
This element defines the formatting options which can be applied to the table background shape. The
background shape is the same size as the entire table and can hold a fill or an effect which spans the entire
table.
[Example: Consider the following example of a table background in use within DrawingML:
<tblBg>
<fillRef idx="2">
<schemeClr val="accent1"/>
</fillRef>
<effectRef idx="1">
<schemeClr val="accent1"/>
</effectRef>
</tblBg>
In this example, we see that there is a themed fill and themed effect being applied to the table background
through the table style. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TableBackgroundStyle) is located in
§A.4.1. end note]
2816 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2827 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.26 tblStyle (Table Style)
This is the root element for a table style. Within the table style are different formatting options available in
order to apply a table.
Attributes Description
styleId (Style ID) Specifies a GUID identifying the table style in a unique manner.
The possible values for this attribute are defined by the ST_Guid simple type (§22.9.2.4).
styleName (Name) Specifies the name of the table style which can show up in the user interface identifying
the style to a user.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TableStyle) is located in §A.4.1. end
note]
20.1.4.2.27 tblStyleLst (Table Style List)
This element is simply a list of table styles which are used within a document.
[Example: Consider the following example of a table style list within DrawingML:
<tblStyleLst def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}">
<tblStyle styleId="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"
styleName="Medium Style 2 - Accent 1">
…
</tblStyle>
<tblStyle styleId="{3C2FFA5D-87B4-456A-9821-1D502468CF0F}"
styleName="Themed Style 1 - Accent 1">
…
</tblStyle>
</tblStyleLst>
In this example, we see two table styles defined along with the default being specified. end example]
Attributes Description
def (Default) The GUID corresponding to the default table style in the list of table styles. This default
can be used when a table is initially inserted into a document.
The possible values for this attribute are defined by the ST_Guid simple type (§22.9.2.4).
©ISO/IEC 2016 – All rights reserved 2817\n\n--- Page 2828 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TableStyleList) is located in §A.4.1.
end note]
20.1.4.2.28 tcBdr (Table Cell Borders)
This element defines the borders for the cells within a table.
[Example: Consider the following example of table cell borders being used within DrawingML:
<tcBdr>
<left>
<lnRef idx="1">
<schemeClr val="accent1"/>
</lnRef>
</left>
<right>
<lnRef idx="1">
<schemeClr val="accent1"/>
</lnRef>
</right>
<top>
<lnRef idx="1">
<schemeClr val="accent1"/>
</lnRef>
</top>
<bottom>
<lnRef idx="2">
<schemeClr val="lt1"/>
</lnRef>
</bottom>
<insideH>
<ln>
<noFill/>
</ln>
</insideH>
<insideV>
<ln>
<noFill/>
</ln>
</insideV>
</tcBdr>
In this example, we define borders for the bottom, top, right, and left borders of the table cells. end example]
2818 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2829 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TableCellBorderStyle) is located in
§A.4.1. end note]
20.1.4.2.29 tcStyle (Table Cell Style)
This element defines the style for a give cell in a table.
[Example: Consider the following example of a table cell style in use within DrawingML:
<tcStyle>
<tcBdr>
…
</tcBdr>
<fill>
…
</fill>
</tcStyle>
In this example, we see that a set of borders for the cell along with a cell fill are being defined. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TableStyleCellStyle) is located in
§A.4.1. end note]
20.1.4.2.30 tcTxStyle (Table Cell Text Style)
This element defines the text properties associated with the text contained within a table cell.
[Example: Consider the following example of a table cell text style in use within DrawingML:
<tcTxStyle b="on">
<fontRef idx="minor">
<scrgbClr r="0" g="0" b="0"/>
</fontRef>
<schemeClr val="lt1"/>
</tcTxStyle>
In this example, we define the text within the cell to be bold and reference the themed minor font and to also
be the light 1 color. end example]
Attributes Description
b (Bold) Specifies if the text is to be bolded.
The possible values for this attribute are defined by the ST_OnOffStyleType simple type
(§20.1.10.36).
i (Italic) Specifies if the text is to be italicized.
The possible values for this attribute are defined by the ST_OnOffStyleType simple type
©ISO/IEC 2016 – All rights reserved 2819\n\n--- Page 2830 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(§20.1.10.36).
[Note: The W3C XML Schema definition of this element’s content model (CT_TableStyleTextStyle) is located in
§A.4.1. end note]
20.1.4.2.31 tl2br (Top Left to Bottom Right Border)
This element defines the line properties associated with the border which goes from the top-left to the bottom-
right corner in a table cell.
[Example: Consider the following example of the top border in use within DrawingML:
<tl2br>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</tl2br>
In this example, we see the border on a table cell to be a single 1pt line which is colored accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.32 top (Top Border)
This element defines the line properties associated with the top border in a table cell.
[Example: Consider the following example of the top border in use within DrawingML:
<top>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</top>
In this example, we see the top border on a table cell to be a single 1pt line which is colored accent 1. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
2820 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2831 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.4.2.33 tr2bl (Top Right to Bottom Left Border)
This element defines the line properties associated with the border which goes from the top-right to the
bottom-left corner in a table cell.
[Example: Consider the following example of the top border in use within DrawingML:
<tr2bl>
<ln w="12700" cmpd="sng">
<solidFill>
<schemeClr val="accent1"/>
</solidFill>
</ln>
</tr2bl>
In this example, we see the border on a table cell to be a single 1pt line which is colored accent 1. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ThemeableLineStyle) is located in
§A.4.1. end note]
20.1.4.2.34 wholeTbl (Whole Table)
This element contains formatting options which are applied to the table as a whole when it is in its default state
with no formatting options (first row, last row, etc) enabled.
[Example: Consider the following example of whole table being used within DrawingML:
<wholeTbl>
<tcTxStyle>
…
</tcTxStyle>
<tcStyle>
…
</tcStyle>
</wholeTbl>
In this example, we see definitions for the text and the cells within the table. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TablePartStyle) is located in §A.4.1.
end note]
20.1.5 3D
The 3D portion of the DrawingML framework allows for the describing of a 3D scene to be placed within a
document. This 3D scene can be described using text and shape objects along with various lighting, material and
camera settings.
©ISO/IEC 2016 – All rights reserved 2821\n\n--- Page 2832 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.5.1 anchor (Anchor Point)
This element specifies a point in 3D space. This point is the point in space that anchors the backdrop plane.
Please see the example in the backdrop (§20.1.5.2) definition for an in depth explanation of this element.
Attributes Description
x (X-Coordinate in X-Coordinate in 3D space.
3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Coordinate in Y-Coordinate in 3D space.
3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
z (Z-Coordinate in Z-Coordinate in 3D space.
3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point3D) is located in §A.4.1. end
note]
20.1.5.2 backdrop (Backdrop Plane)
This element defines a plane in which effects, such as glow and shadow, are applied in relation to the shape they
are being applied to. The points and vectors contained within the backdrop define a plane in 3D space.
[Example: Consider the following image as an explanation of the backdrop plane definition:
2822 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2833 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
In this image we see a plane being defined by an anchor point, the vector normal to the face of the plane and a
vector pointing up in relation to the plane. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Backdrop) is located in §A.4.1. end
note]
20.1.5.3 bevelB (Bottom Bevel)
This element holds the properties associated with defining a bevel on the bottom or back face of a shape.
[Example: Consider the following example of an sp3d containing a bottom bevel.
<a:sp3d>
<a:bevelB w="139700" h="127000" prst="coolSlant"/>
</a:sp3d>
In this example, we see a bottom bevel being defined with a preset bevel type along with a custom width and
height. end example]
Attributes Description
h (Height) Specifies the height of the bevel, or how far above the shape it is applied.
[Example: Consider the following example bevel
In this example, we see the height of an example bevel on a shape. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
prst (Preset Bevel) Specifies the preset bevel type which defines the look of the bevel.
The possible values for this attribute are defined by the ST_BevelPresetType simple type
(§20.1.10.9).
w (Width) Specifies the width of the bevel, or how far into the shape it is applied.
[Example: Consider the following example bevel
©ISO/IEC 2016 – All rights reserved 2823\n\n--- Page 2834 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
In this example, we see the width of an example bevel on a shape. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_Bevel) is located in §A.4.1. end
note]
20.1.5.4 bevelT (Top Bevel)
This element holds the properties associated with defining a bevel on the top or front face of a shape.
[Example: Consider the following example of an sp3d containing a top bevel.
<a:sp3d>
<a:bevelT w="139700" h="127000" prst="coolSlant"/>
</a:sp3d>
In this example, we see a top bevel being defined with a preset bevel type along with a custom width and
height. end example]
Attributes Description
h (Height) Specifies the height of the bevel, or how far above the shape it is applied.
[Example: Consider the following example bevel
In this example, we see the height of an example bevel on a shape. end example]
2824 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2835 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
prst (Preset Bevel) Specifies the preset bevel type which defines the look of the bevel.
The possible values for this attribute are defined by the ST_BevelPresetType simple type
(§20.1.10.9).
w (Width) Specifies the width of the bevel, or how far into the shape it is applied.
[Example: Consider the following example bevel
In this example, we see the width of an example bevel on a shape. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_Bevel) is located in §A.4.1. end
note]
20.1.5.5 camera (Camera)
This element defines the placement and properties of the camera in the 3D scene. The camera position and
properties modify the view of the scene.
[Example: Consider the following example of a camera in DrawingML:
<a:camera prst="orthographicFront">
<a:rot lat="19902513" lon="17826689" rev="1362739"/>
</a:camera>
In this example, we see a preset camera being defined along with a rotation containing latitude, longitude, and
revolution overrides provided that further rotate the camera around the scene. The effect of this camera can
be seen on the following shape:
©ISO/IEC 2016 – All rights reserved 2825\n\n--- Page 2836 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
fov (Field of View) Provides an override for the default field of view for the camera. Different perspectives
can be obtained by modifying this attribute.
[Example: Consider the following example of a fov in DrawingML:
<a:camera prst="perspectiveContrastingRightFacing"
fov="6900000">
<a:rot lat="1200000" lon="18000000" rev="1200000"/>
</a:camera>
In this example, we see a fov being defined which modifies the default fov for the preset
camera. end example]
The possible values for this attribute are defined by the ST_FOVAngle simple type
(§20.1.10.26).
prst (Preset Camera Defines the preset camera that is being used by the camera element. The preset camera
Type) defines a starting point for common preset rotations in space.
[Example: Consider the following example of a prst in DrawingML:
<a:camera prst="perspectiveContrastingRightFacing"
fov="6900000">
<a:rot lat="1200000" lon="18000000" rev="1200000"/>
</a:camera>
In this example, we see a prst being defined as perspectiveContrastingRightFacing.
end example]
The possible values for this attribute are defined by the ST_PresetCameraType simple
type (§20.1.10.47).
zoom (Zoom) Defines the zoom factor of a given camera element. The zoom modifies the scene as a
whole and zooms in or out accordingly.
[Example: Consider the following example of a zoom in DrawingML:
2826 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2837 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<a:camera prst="perspectiveContrastingRightFacing"
fov="6900000" zoom="200%">
<a:rot lat="1200000" lon="18000000" rev="1200000"/>
/a:camera>
In this example, we see a zoom being used which zooms the scene by 200%. end
example]
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_Camera) is located in §A.4.1. end
note]
20.1.5.6 contourClr (Contour Color)
This element defines the color for the contour on a shape. The contour of a shape is a solid filled line which
surrounds the outer edges of the shape.
[Example: Consider the following example of a contour defined on a shape which includes a contourClr.
Lighting characteristics applied to the shape are ignored when it comes to the contour on the shape.
<a:sp3d contourW="101600" prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:contourClr>
<a:schemeClr val="bg1"/>
</a:contourClr>
</a:sp3d>
In this example, we see a contour defined on a shape with a top and bottom bevel defined. In the image below,
the contour is the white ring around the shape.
©ISO/IEC 2016 – All rights reserved 2827\n\n--- Page 2838 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.5.7 extrusionClr (Extrusion Color)
This element defines the color of the extrusion applied to a shape. The extrusion on a shape is an artificial
height applied to the geometry.
[Example: Consider the following example of an extrusion which takes advantage of the extrusionClr. Lighting
characteristics that are applied to the shape are also applied to the extrusion on the shape.
<a:sp3d extrusionH="139700" prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:extrusionClr>
<a:srgbClr val="FF0000"/>
</a:extrusionClr>
</a:sp3d>
In this example, we see the extrusion color defined as red which can also be shown applied to the shape in the
following image:
2828 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2839 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.5.8 flatTx (No text in 3D scene)
Keep text out of 3D scene entirely.
Attributes Description
z (Z Coordinate) Specifies the Z coordinate to be used in positioning the flat text within the 3D scene.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_FlatText) is located in §A.4.1. end
note]
20.1.5.9 lightRig (Light Rig)
This element defines the light rig associated with the table. The light rig comes into play when there is a 3D
bevel applied to a cell. When 3D is used, the light rig defines the lighting properties associated with the scene.
Attributes Description
dir (Direction) Defines the direction from which the light rig is oriented in relation to the scene.
[Example: Consider the following example of dir being used in a light rig:
<a:lightRig rig="threePt" dir="t"/>
In this example, we define the direction to be top. end example]
©ISO/IEC 2016 – All rights reserved 2829\n\n--- Page 2840 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_LightRigDirection simple
type (§20.1.10.29).
rig (Rig Preset) Defines the preset type of light rig which is to be applied to the scene.
[Example: Consider the following example of rig being used in a light rig:
<a:lightRig rig="threePt" dir="t"/>
In this example, we define the rig to be a threePt rig. end example]
The possible values for this attribute are defined by the ST_LightRigType simple type
(§20.1.10.30).
[Note: The W3C XML Schema definition of this element’s content model (CT_LightRig) is located in §A.4.1. end
note]
20.1.5.10 norm (Normal)
This element defines a normal vector. To be more precise, this attribute defines a vector normal to the face of
the backdrop plane.
[Example: Consider the following image as an example of what a normal vector is in relation to the backdrop
plane:
end example]
2830 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2841 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
dx (Distance along Distance along X-axis in 3D
X-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
dy (Distance along Distance along Y-axis in 3D
Y-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
dz (Distance along Distance along Z-axis in 3D
Z-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Vector3D) is located in §A.4.1. end
note]
20.1.5.11 rot (Rotation)
This element defines a rotation in 3D space. A rotation in DrawingML is defined through the use of a latitude
coordinate, a longitude coordinate, and a revolution about the axis as the latitude and longitude coordinates.
[Example: Consider the following example of a rotation defined by the rot elements being used in a lightRig in
DrawingML:
<a:lightRig rig="twoPt" dir="t">
<a:rot lat="0" lon="0" rev="6000000"/>
</a:lightRig>
In this example, we have only a revolution applied to the light rig which rotates it around it's center axis. end
example]
Attributes Description
lat (Latitude) Defines the latitude value of the rotation.
[Example: Consider the following example of a rot in DrawingML:
<a:rot lat="0" lon="0" rev="6000000"/>
In this example, we set the lat to be equal to 0. end example]
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
lon (Longitude) Defines the longitude value of the rotation.
©ISO/IEC 2016 – All rights reserved 2831\n\n--- Page 2842 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: Consider the following example of a rot in DrawingML:
<a:rot lat="0" lon="0" rev="6000000"/>
In this example, we set the lon to be equal to 0. end example]
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
rev (Revolution) This attributes defines the revolution around the central axis in the rotation.
[Example: Consider the following example of a rot in DrawingML:
<a:rot lat="0" lon="0" rev="6000000"/>
In this example, we set the rev to be equal to 6000000. end example]
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
[Note: The W3C XML Schema definition of this element’s content model (CT_SphereCoords) is located in §A.4.1.
end note]
20.1.5.12 sp3d (Apply 3D shape properties)
This element defines the 3D properties associated with a particular shape in DrawingML. The 3D properties
which can be applied to a shape are top and bottom bevels, a contour and an extrusion.
[Example: Consider the following example of an sp3d in DrawingML:
<a:sp3d extrusionH="165100" contourW="50800" prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:extrusionClr>
<a:srgbClr val="FF0000"/>
</a:extrusionClr>
<a:contourClr>
<a:schemeClr val="accent3"/>
</a:contourClr>
</a:sp3d>
In this example, we see an sp3d defined which contains information defining both a top and bottom bevel,
along with an extrusion and contour on the shape. The following image illustrates a shape with the applied
sp3d:
2832 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2843 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
contourW (Contour Defines the width of the contour on the shape.
Width)
[Example: Consider the following example of a contourW in use within the sp3d
element:
<a:sp3d extrusionH="165100" contourW="50800"
prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:extrusionClr>
<a:srgbClr val="FF0000"/>
</a:extrusionClr>
<a:contourClr>
<a:schemeClr val="accent3"/>
</a:contourClr>
</a:sp3d>
In this example, we see a countourW defined as 50800. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
extrusionH Defines the height of the extrusion applied to the shape.
(Extrusion Height)
[Example: Consider the following example of an extrusionH in use within the sp3d
element:
<a:sp3d extrusionH="165100" contourW="50800"
prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:extrusionClr>
<a:srgbClr val="FF0000"/>
©ISO/IEC 2016 – All rights reserved 2833\n\n--- Page 2844 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
</a:extrusionClr>
<a:contourClr>
<a:schemeClr val="accent3"/>
</a:contourClr>
</a:sp3d>
In this example, we see a extrusionH defined as 165100. end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
prstMaterial Defines the preset material which is combined with the lighting properties to give the
(Preset Material final look and feel of a shape.
Type)
[Example: Consider the following example of a prstMaterial in use within the sp3d
element:
<a:sp3d extrusionH="165100" contourW="50800"
prstMaterial="plastic">
<a:bevelT w="254000" h="254000"/>
<a:bevelB w="254000" h="254000"/>
<a:extrusionClr>
<a:srgbClr val="FF0000"/>
</a:extrusionClr>
<a:contourClr>
<a:schemeClr val="accent3"/>
</a:contourClr>
</a:sp3d>
In this example, we see a prstMaterial defined as plastic. end example]
The possible values for this attribute are defined by the ST_PresetMaterialType simple
type (§20.1.10.50).
z (Shape Depth) Defines the z coordinate for the 3D shape.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Shape3D) is located in §A.4.1. end
note]
20.1.5.13 up (Up Vector)
This element defines a vector representing up. To be more precise, this attribute defines a vector representing
up in relation to the face of the backdrop plane.
2834 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2845 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following image as an example of what an up vector is in relation to the backdrop plane:
end example]
Attributes Description
dx (Distance along Distance along X-axis in 3D
X-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
dy (Distance along Distance along Y-axis in 3D
Y-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
dz (Distance along Distance along Z-axis in 3D
Z-axis in 3D)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Vector3D) is located in §A.4.1. end
note]
20.1.6 Shared Style Sheet
The shared style sheet aspects contained within DrawingML are responsible for containing formatting options
and styles which can be used by applications to define a certain look or feel to documents. The shared style
sheet can be used by any document category ([Note: For example, a presentation. end note]) to pull visual
information from which formats the document in a certain way, or theme. The shared style sheet contains
information that is not document-category specific.
©ISO/IEC 2016 – All rights reserved 2835\n\n--- Page 2846 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.6.1 clrMap (Color Map)
This element specifics the color mapping layer which allows a user to define colors for background and text.
This allows for swapping out of light/dark colors for backgrounds and the text on top of the background in order
to maintain readability of the text On a deeper level, this specifies exactly which colors the first 12 values refer
to in the color scheme.
[Example: Consider the following example of a color map in use:
<clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1"
accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5"
accent6="accent6" hlink="hlink" folHlink="folHlink"/>
In this example, we see that bg1 is mapped to lt1, tx1 is mapped to dk1, and so on. end example]
Attributes Description
accent1 (Accent 1) Specifies a color defined which is associated as the accent 1 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent2 (Accent 2) Specifies a color defined which is associated as the accent 2 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent3 (Accent 3) Specifies a color defined which is associated as the accent 3 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent4 (Accent 4) Specifies a color defined which is associated as the accent 4 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent5 (Accent 5) Specifies a color defined which is associated as the accent 5 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent6 (Accent 6) Specifies a color defined which is associated as the accent 6 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
bg1 (Background 1) A color defined which is associated as the first background color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
bg2 (Background 2) Specifies a color defined which is associated as the second background color.
2836 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2847 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
folHlink (Followed Specifies a color defined which is associated as the color for a followed hyperlink.
Hyperlink)
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
hlink (Hyperlink) Specifies a color defined which is associated as the color for a hyperlink.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
tx1 (Text 1) Specifies a color defined which is associated as the first text color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
tx2 (Text 2) Specifies a color defined which is associated as the second text color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorMapping) is located in §A.4.1.
end note]
20.1.6.2 clrScheme (Color Scheme)
This element defines a set of colors which are referred to as a color scheme. The color scheme is responsible for
defining a list of twelve colors. The twelve colors consist of six accent colors, two dark colors, two light colors
and a color for each of a hyperlink and followed hyperlink.
The Color Scheme Color elements appear in a sequence. The following listing shows the index value and
corresponding Color Name.
Sequence Index Element (Color) Name
0 dk1 (Dark 1)
1 lt1 (Light 1)
2 dk2 (Dark 2)
3 lt2 (Light 2)
4 accent1 (Accent 1)
5 accent2 (Accent 2)
6 accent3 (Accent 3)
7 accent4 (Accent 4)
©ISO/IEC 2016 – All rights reserved 2837\n\n--- Page 2848 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Sequence Index Element (Color) Name
8 accent5 (Accent 5)
9 accent6 (Accent 6)
10 hlink (Hyperlink)
11 folHlink (Followed Hyperlink)
[Example: Consider the following example of a color scheme defined in DrawingML:
<clrScheme name="sample">
<dk1>
<sysClr val="windowText"/>
</dk1>
<lt1>
<sysClr val="window"/>
</lt1>
<dk2>
<srgbClr val="04617B"/>
</dk2>
<lt2>
<srgbClr val="DBF5F9"/>
</lt2>
<accent1>
<srgbClr val="0F6FC6"/>
</accent1>
<accent2>
<srgbClr val="009DD9"/>
</accent2>
<accent3>
<srgbClr val="0BD0D9"/>
</accent3>
<accent4>
<srgbClr val="10CF9B"/>
</accent4>
<accent5>
<srgbClr val="7CCA62"/>
</accent5>
<accent6>
<srgbClr val="A5C249"/>
</accent6>
<hlink>
<srgbClr val="FF9800"/>
</hlink>
2838 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2849 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<folHlink>
<srgbClr val="F45511"/>
</folHlink>
</clrScheme>
In this example, are defined the 12 theme colors in the sample color scheme. end example]
Attributes Description
name (Name) The common name for this color scheme. This name can show up in the user interface in
a list of color schemes.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorScheme) is located in §A.4.1.
end note]
20.1.6.3 custClrLst (Custom Color List)
This element allows for a custom color palette to be created and which shows up alongside other color schemes.
This can be very useful, for example, when someone would like to maintain a corporate color palette.
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomColorList) is located in
§A.4.1. end note]
20.1.6.4 extraClrScheme (Extra Color Scheme)
This element defines an auxiliary color scheme, which includes both a color scheme and color mapping. This is
mainly used for backward compatibility concerns and roundtrips information required by earlier versions.
[Example: Consider the following example of an extra color scheme in use in DrawingML:
<extraClrScheme>
<clrScheme name="extraColorSchemeSample">
<dk1>
<sysClr val="windowText"/>
</dk1>
<lt1>
<sysClr val="window"/>
</lt1>
<dk2>
<srgbClr val="04617B"/>
</dk2>
<lt2>
<srgbClr val="DBF5F9"/>
</lt2>
©ISO/IEC 2016 – All rights reserved 2839\n\n--- Page 2850 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<accent1>
<srgbClr val="0F6FC6"/>
</accent1>
<accent2>
<srgbClr val="009DD9"/>
</accent2>
<accent3>
<srgbClr val="0BD0D9"/>
</accent3>
<accent4>
<srgbClr val="10CF9B"/>
</accent4>
<accent5>
<srgbClr val="7CCA62"/>
</accent5>
<accent6>
<srgbClr val="A5C249"/>
</accent6>
<hlink>
<srgbClr val="FF9800"/>
</hlink>
<folHlink>
<srgbClr val="F45511"/>
</folHlink>
</clrScheme>
<clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1"
accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5"
accent6="accent6" hlink="hlink" folHlink="folHlink"/>
</extraClrScheme>
In this example, the extra color scheme contains a color scheme and a color map for that color scheme. end
example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorSchemeAndMapping) is
located in §A.4.1. end note]
20.1.6.5 extraClrSchemeLst (Extra Color Scheme List)
This element is a container for the list of extra color schemes present in a document.
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorSchemeList) is located in
§A.4.1. end note]
2840 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2851 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.6.6 masterClrMapping (Master Color Mapping)
This element is a part of a choice for which color mapping is used within the document. There is also defined an
overrideClrMapping (§20.1.6.8) element which, when specified, the override is used rather than the color
mapping defined in the master. If this element is specified, then we specifically use the color mapping defined
in the master.
[Note: The W3C XML Schema definition of this element’s content model (CT_EmptyElement) is located in §A.4.1.
end note]
20.1.6.7 objectDefaults (Object Defaults)
This element allows for the definition of default shape, line, and textbox formatting properties. An application
can use this information to format a shape (or text) initially on insertion into a document.
[Note: The W3C XML Schema definition of this element’s content model (CT_ObjectStyleDefaults) is located in
§A.4.1. end note]
20.1.6.8 overrideClrMapping (Override Color Mapping)
This element provides an override for the color mapping in a document. When defined, this color mapping is
used in place of the already defined color mapping, or master color mapping. This color mapping is defined in
the same manner as the other mappings within this document.
[Example: Consider the following example of an override color mapping in DrawingML:
<overrideClrMapping bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1"
accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5"
accent6="accent6" hlink="hlink" folHlink="folHlink"/>
end example]
Attributes Description
accent1 (Accent 1) Specifies a color defined which is associated as the accent 1 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent2 (Accent 2) Specifies a color defined which is associated as the accent 2 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent3 (Accent 3) Specifies a color defined which is associated as the accent 3 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent4 (Accent 4) Specifies a color defined which is associated as the accent 4 color.
©ISO/IEC 2016 – All rights reserved 2841\n\n--- Page 2852 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent5 (Accent 5) Specifies a color defined which is associated as the accent 5 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
accent6 (Accent 6) Specifies a color defined which is associated as the accent 6 color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
bg1 (Background 1) A color defined which is associated as the first background color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
bg2 (Background 2) Specifies a color defined which is associated as the second background color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
folHlink (Followed Specifies a color defined which is associated as the color for a followed hyperlink.
Hyperlink)
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
hlink (Hyperlink) Specifies a color defined which is associated as the color for a hyperlink.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
tx1 (Text 1) Specifies a color defined which is associated as the first text color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
tx2 (Text 2) Specifies a color defined which is associated as the second text color.
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
type (§20.1.10.14).
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorMapping) is located in §A.4.1.
end note]
2842 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2853 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.6.9 theme (Theme)
This element defines the root level complex type associated with a shared style sheet (or theme). This element
holds all the different formatting options available to a document through a theme and defines the overall look
and feel of the document when themed objects are used within the document.
[Example: Consider the following image as an example of different themes in use applied to a presentation:
In this example, we see how a theme can affect font, colors, backgrounds, fills, and effects for different objects
in a presentation. end example]
Attributes Description
name (Name) Specifies the name given to the theme.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OfficeStyleSheet) is located in
§A.4.1. end note]
20.1.6.10 themeElements (Theme Elements)
This element defines the theme formatting options for the theme and is the workhorse of the theme. This is
where the bulk of the shared theme information is contained and used by a document. This element contains
the color scheme, font scheme, and format scheme elements which define the different formatting aspects of
what a theme defines.
[Example: Consider the following example of a theme elements defined in DrawingML:
©ISO/IEC 2016 – All rights reserved 2843\n\n--- Page 2854 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<themeElements>
<clrScheme name="sample">
…
</clrScheme>
<fontScheme name="sample">
…
</fontScheme>
<fmtScheme name="sample">
<fillStyleLst>
…
</fillStyleLst>
<lnStyleLst>
…
</lnStyleLst>
<effectStyleLst>
…
</effectStyleLst>
<bgFillStyleLst>
…
</bgFillStyleLst>
</fmtScheme>
</themeElements>
In this example, we see the basic structure of how a theme elements is defined and have left out the true guts of
each individual piece to save room. Each part (color scheme, font scheme, format scheme) is defined elsewhere
within DrawingML. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_BaseStyles) is located in §A.4.1. end
note]
20.1.6.11 themeManager (Theme Manager)
The starting part for a theme file.
[Note: The W3C XML Schema definition of this element’s content model (CT_EmptyElement) is located in §A.4.1.
end note]
20.1.6.12 themeOverride (Theme Override)
This element allows for an override which changes just the colors, fonts, or effects of a single object, like a table
for example. Currently it is used only to control overrides on the non-top-level masters within a presentation.
[Note: The W3C XML Schema definition of this element’s content model (CT_BaseStylesOverride) is located in
§A.4.1. end note]
2844 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2855 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.7 Coordinate Systems and Transformations
The following elements are used to reflect dimensions, scaling, location, rotation, and flip information on groups
and individual shapes respectively.
20.1.7.1 chExt (Child Extents)
This element specifies the size dimensions of the child extents rectangle and is used for calculations of grouping,
scaling, and rotation behavior of shapes placed within a group.
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
<… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
< … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
20.1.7.2 chOff (Child Offset)
This element specifies the location of the child extents rectangle and is used for calculations of grouping, scaling,
and rotation behavior of shapes placed within a group.
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
©ISO/IEC 2016 – All rights reserved 2845\n\n--- Page 2856 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Coordinate) by the parent XML element.
[Example: Consider the following point on a basic wrapping polygon for a DrawingML
object:
<… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
[Example: Consider the following point on a basic wrapping polygon for a DrawingML
object:
<… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
20.1.7.3 ext (Extents)
This element specifies the size of the bounding box enclosing the referenced object.
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
<… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
2846 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2857 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
< … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
20.1.7.4 off (Offset)
This element specifies the location of the bounding box of an object. Effects on an object are not included in this
bounding box.
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
[Example: Consider the following point on a basic wrapping polygon for a DrawingML
object:
<… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
[Example: Consider the following point on a basic wrapping polygon for a DrawingML
object:
<… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
©ISO/IEC 2016 – All rights reserved 2847\n\n--- Page 2858 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
20.1.7.5 xfrm (2D Transform for Grouped Objects)
This element is nearly identical to the representation of 2-D transforms for ordinary shapes (§20.1.7.6). The only
addition is a member to represent the Child offset and the Child extents.
Attributes Description
flipH (Horizontal Horizontal flip. When true, this attribute defines that the group is flipped horizontally
Flip) about the center of its bounding box.
[Example: The following illustrates the effect of a horizontal flip.
Unflipped flipH True
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
flipV (Vertical Flip) Vertical flip. When true, this attribute defines that the group is flipped vertically about
the center of its bounding box.
[Example: The following illustrates the effect of a vertical flip.
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
rot (Rotation) Rotation. Specifies the clockwise rotation of a group in 1/64000 of a degree.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
2848 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2859 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupTransform2D) is located in
§A.4.1. end note]
20.1.7.6 xfrm (2D Transform for Individual Objects)
This element represents 2-D transforms for ordinary shapes.
Attributes Description
flipH (Horizontal Specifies a horizontal flip. When true, this attribute defines that the shape is flipped
Flip) horizontally about the center of its bounding box.
[Example: The following illustrates the effect of a horizontal flip.
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
flipV (Vertical Flip) Specifies a vertical flip. When true, this attribute defines that the group is flipped
vertically about the center of its bounding box.
[Example: The following illustrates the effect of a vertical flip.
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
rot (Rotation) Specifies the rotation of the Graphic Frame. The units for which this attribute is specified
in reside within the simple type definition referenced below.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_Transform2D) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2849\n\n--- Page 2860 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8 Shape Fills, Effects, and Line Properties
This portion of the DrawingML framework describes effects defining the visual appearance of shapes and lines.
Shapes can be filled in a variety of ways, with images, solid colors, gradients, or pattern fills. In addition, several
visual effects can alter the appearance of a shape, and multiple effects can be combined together. Lines also
can have special properties defining how they are rendered, included a dashed appearance or decorations at the
line ends. This section documents the elements that define these properties and effects for shapes and lines.
20.1.8.1 alphaBiLevel (Alpha Bi-Level Effect)
This element represents an Alpha Bi-Level Effect.
Alpha (Opacity) values less than the threshold are changed to 0 (fully transparent) and alpha values greater than
or equal to the threshold are changed to 100% (fully opaque).
Attributes Description
thresh (Threshold) Specifies the threshold value for the alpha bi-level effect.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaBiLevelEffect) is located in
§A.4.1. end note]
20.1.8.2 alphaCeiling (Alpha Ceiling Effect)
This element represents an alpha ceiling effect.
Alpha (opacity) values greater than zero are changed to 100%. In other words, anything partially opaque
becomes fully opaque.
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaCeilingEffect) is located in
§A.4.1. end note]
20.1.8.3 alphaFloor (Alpha Floor Effect)
This element represents an alpha floor effect.
Alpha (opacity) values less than 100% are changed to zero. In other words, anything partially transparent
becomes fully transparent.
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaFloorEffect) is located in
§A.4.1. end note]
20.1.8.4 alphaInv (Alpha Inverse Effect)
This element represents an alpha inverse effect.
2850 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2861 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Alpha (opacity) values are inverted by subtracting from 100%.
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaInverseEffect) is located in
§A.4.1. end note]
20.1.8.5 alphaMod (Alpha Modulate Effect)
This element represents an alpha modulate effect.
Effect alpha (opacity) values are multiplied by a fixed percentage. The effect container specifies an effect
containing alpha values to modulate.
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaModulateEffect) is located in
§A.4.1. end note]
20.1.8.6 alphaModFix (Alpha Modulate Fixed Effect)
This element represents an alpha modulate fixed effect.
Effect alpha (opacity) values are multiplied by a fixed percentage.
Attributes Description
amt (Amount) Specifies the percentage amount to scale the alpha.
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaModulateFixedEffect) is
located in §A.4.1. end note]
20.1.8.7 alphaOutset (Alpha Inset/Outset Effect)
This element specifies an alpha outset/inset effect.
This is equivalent to an alpha ceiling, followed by alpha blur, followed by either an alpha ceiling (positive radius)
or alpha floor (negative radius).
Attributes Description
rad (Radius) Specifies the radius of outset/inset.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaOutsetEffect) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2851\n\n--- Page 2862 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.8 alphaRepl (Alpha Replace Effect)
This element specifies an alpha replace effect.
Effect alpha (opacity) values are replaced by a fixed alpha.
Attributes Description
a (Alpha) Specifies the new opacity value.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_AlphaReplaceEffect) is located in
§A.4.1. end note]
20.1.8.9 bevel (Line Join Bevel)
This element specifies a Bevel Line Join.
A bevel joint specifies that an angle joint is used to connect lines.
[Example:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_LineJoinBevel) is located in §A.4.1.
end note]
20.1.8.10 bgClr (Background color)
This element specifies the background color of a Pattern fill.
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.8.11 biLevel (Bi-Level (Black/White) Effect)
This element specifies a bi-level (black/white) effect. Input colors whose luminance is less than the specified
threshold value are changed to black. Input colors whose luminance are greater than or equal the specified
value are set to white. The alpha effect values are unaffected by this effect.
Attributes Description
thresh (Threshold) Specifies the luminance threshold for the Bi-Level effect. Values greater than or equal to
the threshold are set to white. Values lesser than the threshold are set to black.
2852 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2863 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_BiLevelEffect) is located in §A.4.1.
end note]
20.1.8.12 blend (Blend Effect)
This element specifies a blend of several effects. The container specifies the raw effects to blend while the blend
mode specifies how the effects are to be blended.
Attributes Description
blend (Blend Mode) Specifies how to blend the two effects.
The possible values for this attribute are defined by the ST_BlendMode simple type
(§20.1.10.11).
[Note: The W3C XML Schema definition of this element’s content model (CT_BlendEffect) is located in §A.4.1.
end note]
20.1.8.13 blip (Blip)
This element specifies the existence of an image (binary large image or picture) and contains a reference to the
image data.
Attributes Description
cstate Specifies the compression state with which the picture is stored. This allows the
(Compression State) application to specify the amount of compression that has been applied to a picture.
The possible values for this attribute are defined by the ST_BlipCompression simple type
(§20.1.10.12).
embed (Embedded Specifies the identification information for an embedded picture. This attribute is used to
Picture Reference) specify an image that resides locally within the file.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
link (Linked Picture Specifies the identification information for a linked picture. This attribute is used to
Reference) specify an image that does not reside within this file.
©ISO/IEC 2016 – All rights reserved 2853\n\n--- Page 2864 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_Blip) is located in §A.4.1. end note]
20.1.8.14 blipFill (Picture Fill)
This element specifies the type of picture fill that the picture object has. Because a picture has a picture fill
already by default, it is possible to have two fills specified for a picture object. An example of this is shown
below.
[Example: Consider the picture below that has a blip fill applied to it. The image used to fill this picture object
has transparent pixels instead of white pixels.
<p:pic>
…
<p:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</p:blipFill>
…
</p:pic>
The above picture object is shown as an example of this fill type. end example]
2854 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2865 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider now the same picture object but with an additional gradient fill applied within the shape
properties portion of the picture.
<p:pic>
…
<p:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</p:blipFill>
<p:spPr>
<a:gradFill>
<a:gsLst>
<a:gs pos="0">
<a:schemeClr val="tx2">
<a:shade val="50000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="39999">
<a:schemeClr val="tx2">
<a:tint val="20000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="70000">
<a:srgbClr val="C4D6EB"/>
</a:gs>
<a:gs pos="100000">
<a:schemeClr val="bg1"/>
</a:gs>
</a:gsLst>
</a:gradFill>
</p:spPr>
…
</p:pic>
©ISO/IEC 2016 – All rights reserved 2855\n\n--- Page 2866 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The above picture object is shown as an example of this double fill type. end example]
Attributes Description
dpi (DPI Setting) Specifies the DPI (dots per inch) used to calculate the size of the blip. If not present or
zero, the DPI in the blip is used.
[Note: This attribute is primarily used to keep track of the picture quality within a
document. There are different levels of quality needed for print than on-screen viewing
and thus a need to track this information. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
rotWithShape Specifies that the fill should rotate with the shape. That is, when the shape that has been
(Rotate With Shape) filled with a picture and the containing shape (say a rectangle) is transformed with a
rotation then the fill is transformed with the same rotation.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_BlipFillProperties) is located in
§A.4.1. end note]
20.1.8.15 blur (Blur Effect)
This element specifies a blur effect that is applied to the entire shape, including its fill. All color channels,
including alpha, are affected.
Attributes Description
grow (Grow Specifies whether the bounds of the object should be grown as a result of the blurring.
Bounds) True indicates the bounds are grown while false indicates that they are not.
[Example:
2856 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2867 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
With grow set to false, the blur effect does not extend beyond the original bounds of the
object:
With grow set to true, the blur effect can extend beyond the original bounds of the
object:
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
rad (Radius) Specifies the radius of blur.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_BlurEffect) is located in §A.4.1. end
note]
20.1.8.16 clrChange (Color Change Effect)
This element specifies a Color Change Effect. Instances of clrFrom are replaced with instances of clrTo.
Attributes Description
useA (Consider Specifies whether alpha values are considered for the effect. Effect alpha values are
Alpha Values) considered if useA is true, else they are ignored.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
©ISO/IEC 2016 – All rights reserved 2857\n\n--- Page 2868 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorChangeEffect) is located in
§A.4.1. end note]
20.1.8.17 clrFrom (Change Color From)
This element specifies a color getting removed in a color change effect. It is the "from" or source input color.
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.8.18 clrRepl (Solid Color Replacement)
This element specifies a solid color replacement value. All effect colors are changed to a fixed color. Alpha values
are unaffected.
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorReplaceEffect) is located in
§A.4.1. end note]
20.1.8.19 clrTo (Change Color To)
This element specifies the color which replaces the clrFrom in a clrChange effect. This is the "target" or "to"
color in the color change effect.
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.8.20 cont (Effect Container)
This element specifies an Effect Container. It is a list of effects.
Attributes Description
name (Name) Specifies an optional name for this list of effects, so that it can be referred to later. Shall
be unique across all effect trees and effect containers.
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
type (Effect Specifies the kind of container, either sibling or tree.
Container Type)
The possible values for this attribute are defined by the ST_EffectContainerType simple
type (§20.1.10.22).
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectContainer) is located in
§A.4.1. end note]
20.1.8.21 custDash (Custom Dash)
This element specifies a custom dashing scheme. It is a list of dash stop elements which represent building block
atoms upon which the custom dashing scheme is built.
2858 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2869 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_DashStopList) is located in §A.4.1.
end note]
20.1.8.22 ds (Dash Stop)
This element specifies a dash stop primitive. Dashing schemes are built by specifying an ordered list of dash stop
primitive. A dash stop primitive consists of a dash and a space.
Attributes Description
d (Dash Length) Specifies the length of the dash relative to the line width.
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
sp (Space Length) Specifies the length of the space relative to the line width.
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_DashStop) is located in §A.4.1. end
note]
20.1.8.23 duotone (Duotone Effect)
This element specifies a duotone effect.
For each pixel, combines clr1 and clr2 through a linear interpolation to determine the new color for that pixel.
[Note: The W3C XML Schema definition of this element’s content model (CT_DuotoneEffect) is located in §A.4.1.
end note]
20.1.8.24 effect (Effect)
This element specifies a reference to an existing effect container.
Attributes Description
ref (Reference) Specifies the reference. Its value can be the name of an effect container, or one of four
special references:
fill - refers to the fill effect
line - refers to the line effect
fillLine - refers to the combined fill and line effects
children - refers to the combined effects from logical child shapes or text
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
©ISO/IEC 2016 – All rights reserved 2859\n\n--- Page 2870 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectReference) is located in
§A.4.1. end note]
20.1.8.25 effectDag (Effect Container)
This element specifies a list of effects. Effects are applied in the order specified by the container type (sibling or
tree).
[Note: An effectDag element can contain multiple effect containers as child elements. Effect containers with
different styles can be combined in an effectDag to define a directed acyclic graph (DAG) that specifies the order
in which all effects are applied. end note]
Attributes Description
name (Name) Specifies an optional name for this list of effects, so that it can be referred to later. Shall
be unique across all effect trees and effect containers.
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
type (Effect Specifies the kind of container, either sibling or tree.
Container Type)
The possible values for this attribute are defined by the ST_EffectContainerType simple
type (§20.1.10.22).
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectContainer) is located in
§A.4.1. end note]
20.1.8.26 effectLst (Effect Container)
This element specifies a list of effects. Effects in an effectLst are applied in the default order by the rendering
engine. The following diagrams illustrate the order in which effects are applied, both for shapes and for group
shapes.
[Note: The output of many effects does not include the input shape. For effects that should be applied to the
result of previous effects as well as the original shape, a container is used to group the inputs together. end
note]
[Example: Outer Shadow is applied both to the original shape and the original shape's glow. The result of blur
contains the original shape, while the result of glow contains only the added glow. Therefore, a container that
groups the blur result with the glow result is used as the input to Outer Shadow. end example]
2860 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2871 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
effectLst Processing for Shapes
Shape Fill and
Shape Line
Picture Correction
Fill Overlay
Inner Shadow
Container Preset Shadow
Soft Edges
Blur
Glow
Container
Outer Shadow
Container
Reflection
Final Output
©ISO/IEC 2016 – All rights reserved 2861\n\n--- Page 2872 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
effectLst Processing for Group Shapes
Group Shape
Soft Edges
Blur
Glow
Container
Outer Shadow
Container
Reflection
Final Output
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectList) is located in §A.4.1. end
note]
20.1.8.27 fgClr (Foreground color)
This element specifies the foreground color of a pattern fill.
2862 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2873 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
20.1.8.28 fill (Fill)
This element specifies a fill which is one of blipFill, gradFill, grpFill, noFill, pattFill or solidFill.
[Note: The W3C XML Schema definition of this element’s content model (CT_FillEffect) is located in §A.4.1. end
note]
20.1.8.29 fillOverlay (Fill Overlay Effect)
This element specifies a fill overlay effect. A fill overlay can be used to specify an additional fill for an object and
blend the two fills together.
Attributes Description
blend (Blend) Specifies how to blend the fill with the base effect.
The possible values for this attribute are defined by the ST_BlendMode simple type
(§20.1.10.11).
[Note: The W3C XML Schema definition of this element’s content model (CT_FillOverlayEffect) is located in
§A.4.1. end note]
20.1.8.30 fillRect (Fill Rectangle)
This element specifies a fill rectangle. When stretching of an image is specified, a source rectangle, srcRect, is
scaled to fit the specified fill rectangle.
Each edge of the fill rectangle is defined by a percentage offset from the corresponding edge of the shape's
bounding box. A positive percentage specifies an inset, while a negative percentage specifies an outset. [Note:
For example, a left offset of 25% specifies that the left edge of the fill rectangle is located to the right of the
bounding box's left edge by an amount equal to 25% of the bounding box's width. end note]
[Example:
<a:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect b="10000" r="25000"/>
©ISO/IEC 2016 – All rights reserved 2863\n\n--- Page 2874 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</a:stretch>
</a:blipFill>
The above image is stretched to fill the entire rectangle except for the bottom 10% and rightmost 25%.
end example]
Attributes Description
b (Bottom Offset) Specifies the bottom edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
l (Left Offset) Specifies the left edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
r (Right Offset) Specifies the right edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
t (Top Offset) Specifies the top edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_RelativeRect) is located in §A.4.1.
end note]
20.1.8.31 fillToRect (Fill To Rectangle)
This element defines the "focus" rectangle for the center shade, specified relative to the fill tile rectangle. The
center shade fills the entire tile except the margins specified by each attribute.
Each edge of the center shade rectangle is defined by a percentage offset from the corresponding edge of the
tile rectangle. A positive percentage specifies an inset, while a negative percentage specifies an outset. [Note:
For example, a left offset of 25% specifies that the left edge of the center shade rectangle is located to the right
of the tile rectangle's left edge by an amount equal to 25% of the tile rectangle's width. end note]
[Example:
2864 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2875 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:path path="rect">
<a:fillToRect l="50000" r="50000" t="50000" b="50000"/>
</a:path>
In the above shape, the rectangle defined by fillToRect is a single point in the center of the shape. This creates
the effect of the center shade focusing at a point in the center of the region.
end example]
[Example:
<a:path path="rect">
<a:fillToRect l="25000" t="25000" r="25000" b="0"/>
</a:path>
The center shade occupies the rectangle defined by excluding the topmost, leftmost, and rightmost 25% of the
region. Therefore, the gradient fills the remaining leftmost 25%, topmost 25%, and rightmost 25% of the region.
end example]
Attributes Description
b (Bottom Offset) Specifies the bottom edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
l (Left Offset) Specifies the left edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
r (Right Offset) Specifies the right edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
t (Top Offset) Specifies the top edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_RelativeRect) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2865\n\n--- Page 2876 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.32 glow (Glow Effect)
This element specifies a glow effect, in which a color blurred outline is added outside the edges of the object.
Attributes Description
rad (Radius) Specifies the radius of the glow.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_GlowEffect) is located in §A.4.1.
end note]
20.1.8.33 gradFill (Gradient Fill)
This element defines a gradient fill.
A gradient fill is a fill which is characterized by a smooth gradual transition from one color to the next. At its
simplest, it is a fill which transitions between two colors; or more generally, it can be a transition of any number
of colors.
The desired transition colors and locations are defined in the gradient stop list (gsLst) child element.
The other child element defines the properties of the gradient fill (there are two styles-- a linear shade style as
well as a path shade style)
[Example:
The following is a sample gradient fill, varying from blue to white:
end example]
Attributes Description
flip (Tile Flip) Specifies the direction(s) in which to flip the gradient while tiling.
Normally a gradient fill encompasses the entire bounding box of the shape which
contains the fill. However, with the tileRect element, it is possible to define a "tile"
rectangle which is smaller than the bounding box. In this situation, the gradient fill is
encompassed within the tile rectangle, and the tile rectangle is tiled across the bounding
box to fill the entire area.
2866 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2877 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_TileFlipMode simple type
(§20.1.10.86).
rotWithShape Specifies if a fill rotates along with a shape when the shape is rotated.
(Rotate With Shape)
[Example:
The following is a fill with the flip attribute set to "x". The black interior rectangle
indicates the tile rectangle. Notice that the adjacent rectangle to the right in the tile has
been flipped along the x-axis.
Unrotated Shape
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_GradientFillProperties) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2867\n\n--- Page 2878 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.34 grayscl (Gray Scale Effect)
This element specifies a gray scale effect. Converts all effect color values to a shade of gray, corresponding to
their luminance. Effect alpha (opacity) values are unaffected.
[Note: The W3C XML Schema definition of this element’s content model (CT_GrayscaleEffect) is located in
§A.4.1. end note]
20.1.8.35 grpFill (Group Fill)
This element specifies a group fill. When specified, this setting indicates that the parent element is part of a
group and should inherit the fill properties of the group.
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupFillProperties) is located in
§A.4.1. end note]
20.1.8.36 gs (Gradient stops)
This element defines a gradient stop. A gradient stop consists of a position where the stop appears in the color
band.
Attributes Description
pos (Position) Specifies where this gradient stop should appear in the color band. This position is
specified in the range [0%, 100%], which corresponds to the beginning and the end of the
color band respectively.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_GradientStop) is located in §A.4.1.
end note]
20.1.8.37 gsLst (Gradient Stop List)
The list of gradient stops that specifies the gradient colors and their relative positions in the color band.
[Note: The W3C XML Schema definition of this element’s content model (CT_GradientStopList) is located in
§A.4.1. end note]
20.1.8.38 headEnd (Line Head/End Style)
This element specifies decorations which can be added to the head of a line.
[Example:
2868 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2879 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end exmaple]
Attributes Description
len (Length of Specifies the line end length in relation to the line width.
Head/End)
The possible values for this attribute are defined by the ST_LineEndLength simple type
(§20.1.10.32).
type (Line Specifies the line end decoration, such as a triangle or arrowhead.
Head/End Type)
The possible values for this attribute are defined by the ST_LineEndType simple type
(§20.1.10.33).
w (Width of Specifies the line end width in relation to the line width.
Head/End)
The possible values for this attribute are defined by the ST_LineEndWidth simple type
(§20.1.10.34).
[Note: The W3C XML Schema definition of this element’s content model (CT_LineEndProperties) is located in
§A.4.1. end note]
20.1.8.39 hsl (Hue Saturation Luminance Effect)
This element specifies a hue/saturation/luminance effect. The hue, saturation, and luminance can each be
adjusted relative to its current value.
Attributes Description
hue (Hue) Specifies the number of degrees by which the hue is adjusted.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
lum (Luminance) Specifies the percentage by which the luminance is adjusted.
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
sat (Saturation) Specifies the percentage by which the saturation is adjusted.
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_HSLEffect) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 2869\n\n--- Page 2880 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.40 innerShdw (Inner Shadow Effect)
This element specifies an inner shadow effect. A shadow is applied within the edges of the object according to
the parameters given by the attributes.
Inner Shadow
Attributes Description
blurRad (Blur Specifies the blur radius.
Radius)
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
dir (Direction) Specifies the direction to offset the shadow.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
dist (Distance) Specifies how far to offset the shadow.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_InnerShadowEffect) is located in
§A.4.1. end note]
20.1.8.41 lin (Linear Gradient Fill)
This element specifies a linear gradient.
Attributes Description
ang (Angle) Specifies the direction of color change for the gradient. To define this angle, let its value
be x measured clockwise. Then ( -sin x, cos x ) is a vector parallel to the line of constant
color in the gradient fill.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
scaled (Scaled) Whether the gradient angle scales with the fill region. Mathematically, if this flag is true,
then the gradient vector ( cos x , sin x ) is scaled by the width (w) and height (h) of the fill
region, so that the vector becomes ( w cos x, h sin x ) (before normalization). Observe
that now if the gradient angle is 45 degrees, the gradient vector is ( w, h ), which goes
2870 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2881 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
from top-left to bottom-right of the fill region. If this flag is false, the gradient angle is
independent of the fill region and is not scaled using the manipulation described above.
So a 45-degree gradient angle always give a gradient band whose line of constant color is
parallel to the vector (1, -1).
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_LinearShadeProperties) is located
in §A.4.1. end note]
20.1.8.42 lum (Luminance Effect)
This element specifies a luminance effect. Brightness linearly shifts all colors closer to white or black.
Contrast scales all colors to be either closer or further apart.
Attributes Description
bright (Brightness) Specifies the percent to change the brightness.
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
contrast (Contrast) Specifies the percent to change the contrast.
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_LuminanceEffect) is located in
§A.4.1. end note]
20.1.8.43 miter (Miter Line Join)
This element specifies that a line join shall be mitered.
[Example: The following sample illustrated two lines which are joined using a mitered style
end example]
Attributes Description
lim (Miter Join Specifies the amount by which lines is extended to form a miter join - otherwise miter
©ISO/IEC 2016 – All rights reserved 2871\n\n--- Page 2882 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Limit) joins can extend infinitely far (for lines which are almost parallel).
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_LineJoinMiterProperties) is located
in §A.4.1. end note]
20.1.8.44 noFill (No Fill)
This element specifies that no fill is applied to the parent element.
[Note: The W3C XML Schema definition of this element’s content model (CT_NoFillProperties) is located in
§A.4.1. end note]
20.1.8.45 outerShdw (Outer Shadow Effect)
This element specifies an Outer Shadow Effect.
[Example: The following is an example of an outer shadow effect.
Outer Shadow
end example]
Attributes Description
algn (Shadow Specifies shadow alignment; alignment happens first, effectively setting the origin for
Alignment) scale, skew, and offset.
The possible values for this attribute are defined by the ST_RectAlignment simple type
(§20.1.10.53).
blurRad (Blur Specifies the blur radius of the shadow.
Radius)
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
dir (Shadow Specifies the direction to offset the shadow.
Direction)
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
2872 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2883 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
type (§20.1.10.44).
dist (Shadow Offset Specifies the how far to offset the shadow.
Distance)
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
kx (Horizontal Specifies the horizontal skew angle.
Skew)
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
ky (Vertical Skew) Specifies the vertical skew angle.
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
rotWithShape Specifies whether the shadow rotates with the shape if the shape is rotated.
(Rotate With Shape)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
sx (Horizontal Specifies the horizontal scaling factor; negative scaling causes a flip.
Scaling Factor)
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
sy (Vertical Scaling Specifies the vertical scaling factor; negative scaling causes a flip.
Factor)
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_OuterShadowEffect) is located in
§A.4.1. end note]
20.1.8.46 path (Path Gradient)
This element defines that a gradient fill follows a path vs. a linear line.
[Example:
©ISO/IEC 2016 – All rights reserved 2873\n\n--- Page 2884 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Circle Rect Shape
The examples above illustrate gradient fills following a circular, rectangular or shape path.
end example]
Attributes Description
path (Gradient Fill Specifies the shape of the path to follow.
Path)
The possible values for this attribute are defined by the ST_PathShadeType simple type
(§20.1.10.38).
[Note: The W3C XML Schema definition of this element’s content model (CT_PathShadeProperties) is located in
§A.4.1. end note]
20.1.8.47 pattFill (Pattern Fill)
This element specifies a pattern fill. A repeated pattern is used to fill the object.
Attributes Description
prst (Preset Specifies one of a set of preset patterns to fill the object.
Pattern)
The possible values for this attribute are defined by the ST_PresetPatternVal simple type
(§20.1.10.51).
[Note: The W3C XML Schema definition of this element’s content model (CT_PatternFillProperties) is located in
§A.4.1. end note]
20.1.8.48 prstDash (Preset Dash)
This element specifies that a preset line dashing scheme should be used.
Attributes Description
val (Value) Specifies which preset dashing scheme is to be used.
The possible values for this attribute are defined by the ST_PresetLineDashVal simple
type (§20.1.10.49).
2874 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2885 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_PresetLineDashProperties) is
located in §A.4.1. end note]
20.1.8.49 prstShdw (Preset Shadow)
This element specifies that a preset shadow is to be used. Each preset shadow is equivalent to a specific outer
shadow effect. For each preset shadow, the color element, direction attribute, and distance attribute represent
the color, direction, and distance parameters of the corresponding outer shadow. Additionally, the
rotateWithShape attribute of corresponding outer shadow is always false. Other non-default parameters of
the outer shadow are dependent on the prst attribute.
Attributes Description
dir (Direction) Specifies the direction to offset the shadow.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
dist (Distance) Specifies how far to offset the shadow.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
prst (Preset Specifies which preset shadow to use.
Shadow)
The possible values for this attribute are defined by the ST_PresetShadowVal simple
type (§20.1.10.52).
[Note: The W3C XML Schema definition of this element’s content model (CT_PresetShadowEffect) is located in
§A.4.1. end note]
20.1.8.50 reflection (Reflection Effect)
This element specifies a reflection effect.
[Example:
©ISO/IEC 2016 – All rights reserved 2875\n\n--- Page 2886 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Reflection Effect
end example]
Attributes Description
algn (Shadow Specifies shadow alignment.
Alignment)
The possible values for this attribute are defined by the ST_RectAlignment simple type
(§20.1.10.53).
blurRad (Blur Specifies the blur radius.
Radius)
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
dir (Direction) Specifies the direction of the alpha gradient ramp relative to the shape itself.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
dist (Distance) Specifies how far to distance the shadow.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
endA (End Alpha) Specifies the ending reflection opacity.
2876 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2887 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
endPos (End Specifies the end position (along the alpha gradient ramp) of the end alpha value.
Position)
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
fadeDir (Fade Specifies the direction to offset the reflection.
Direction)
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
kx (Horizontal Specifies the horizontal skew angle.
Skew)
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
ky (Vertical Skew) Specifies the vertical skew angle.
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
rotWithShape Specifies if the reflection rotates with the shape.
(Rotate With Shape)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
stA (Start Opacity) starting reflection opacity.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
stPos (Start Specifies the start position (along the alpha gradient ramp) of the start alpha value.
Position)
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
sx (Horizontal Ratio) Specifies the horizontal scaling factor.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
sy (Vertical Ratio) Specifies the vertical scaling factor.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_ReflectionEffect) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2877\n\n--- Page 2888 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.51 relOff (Relative Offset Effect)
This element specifies a relative offset effect. Sets up a new origin by offsetting relative to the size of the
previous effect.
Attributes Description
tx (Offset X) Specifies the X offset.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
ty (Offset Y) Specifies the Y offset.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_RelativeOffsetEffect) is located in
§A.4.1. end note]
20.1.8.52 round (Round Line Join)
This element specifies that lines joined together have a round join.
[Example:
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_LineJoinRound) is located in §A.4.1.
end note]
20.1.8.53 softEdge (Soft Edge Effect)
This element specifies a soft edge effect. The edges of the shape are blurred, while the fill is not affected.
Attributes Description
rad (Radius) Specifies the radius of blur to apply to the edges.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_SoftEdgesEffect) is located in
§A.4.1. end note]
2878 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2889 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.54 solidFill (Solid Fill)
This element specifies a solid color fill. The shape is filled entirely with the specified color.
[Note: The W3C XML Schema definition of this element’s content model (CT_SolidColorFillProperties) is located
in §A.4.1. end note]
20.1.8.55 srcRect (Source Rectangle)
This element specifies the portion of the blip used for the fill.
Each edge of the source rectangle is defined by a percentage offset from the corresponding edge of the
bounding box. A positive percentage specifies an inset, while a negative percentage specifies an outset. [Note:
For example, a left offset of 25% specifies that the left edge of the source rectangle is located to the right of the
bounding box's left edge by an amount equal to 25% of the bounding box's width. end note]
Attributes Description
b (Bottom Offset) Specifies the bottom edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
l (Left Offset) Specifies the left edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
r (Right Offset) Specifies the right edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
t (Top Offset) Specifies the top edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_RelativeRect) is located in §A.4.1.
end note]
20.1.8.56 stretch (Stretch)
This element specifies that a BLIP should be stretched to fill the target rectangle. The other option is a tile where
a BLIP is tiled to fill the available area.
[Note: The W3C XML Schema definition of this element’s content model (CT_StretchInfoProperties) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2879\n\n--- Page 2890 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.57 tailEnd (Tail line end style)
This element specifies decorations which can be added to the tail of a line.
[Example:
end example]
Attributes Description
len (Length of Specifies the line end length in relation to the line width.
Head/End)
The possible values for this attribute are defined by the ST_LineEndLength simple type
(§20.1.10.32).
type (Line Specifies the line end decoration, such as a triangle or arrowhead.
Head/End Type)
The possible values for this attribute are defined by the ST_LineEndType simple type
(§20.1.10.33).
w (Width of Specifies the line end width in relation to the line width.
Head/End)
The possible values for this attribute are defined by the ST_LineEndWidth simple type
(§20.1.10.34).
[Note: The W3C XML Schema definition of this element’s content model (CT_LineEndProperties) is located in
§A.4.1. end note]
20.1.8.58 tile (Tile)
This element specifies that a BLIP should be tiled to fill the available space. This element defines a "tile"
rectangle within the bounding box. The image is encompassed within the tile rectangle, and the tile rectangle is
tiled across the bounding box to fill the entire area.
[Example:
The following is a fill with the flip attribute set to "x". The black interior rectangle indicates the tile rectangle.
Notice that the adjacent rectangle to the right in the tile has been flipped along the x-axis.
2880 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2891 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
algn (Alignment) Specifies where to align the first tile with respect to the shape. Alignment happens after
the scaling, but before the additional offset.
The possible values for this attribute are defined by the ST_RectAlignment simple type
(§20.1.10.53).
flip (Tile Flipping) Specifies the direction(s) in which to flip the source image while tiling. Images can be
flipped horizontally, vertically, or in both directions to fill the entire region.
The possible values for this attribute are defined by the ST_TileFlipMode simple type
(§20.1.10.86).
sx (Horizontal Ratio) Specifies the amount to horizontally scale the srcRect.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
sy (Vertical Ratio) Specifies the amount to vertically scale the srcRect.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
tx (Horizontal Specifies additional horizontal offset after alignment.
Offset)
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
ty (Vertical Offset) Specifies additional vertical offset after alignment.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_TileInfoProperties) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2881\n\n--- Page 2892 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.8.59 tileRect (Tile Rectangle)
This element specifies a rectangular region of the shape to which the gradient is applied. This region is then
tiled across the remaining area of the shape to complete the fill. The tile rectangle is defined by percentage
offsets from the sides of the shape's bounding box.
Each edge of the tile rectangle is defined by a percentage offset from the corresponding edge of the bounding
box. A positive percentage specifies an inset, while a negative percentage specifies an outset. [Note: For
example, a left offset of 25% specifies that the left edge of the tile rectangle is located to the right of the
bounding box's left edge by an amount equal to 25% of the bounding box's width. end note]
[Example:
The image above depicts a horizontal gradient with no tileRect element.
The image above depicts the same gradient with a tileRect element specifying l="50000" (50%). The right half
of the shape is the tile to which the gradient is applied, and the left half of the shape contains a tiled copy of that
gradient fill.
The image above depicts the same gradient with a tileRect element specifying l="75000" (75%). The rightmost
25% of the shape contains the tile rectangle to which the gradient is applied. This gradient is tiled three times to
cover the leftmost 75% of the shape. The tile rectangle is flipped horizontally when covering the shape.
end example]
Attributes Description
b (Bottom Offset) Specifies the bottom edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
2882 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2893 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(§20.1.10.40).
l (Left Offset) Specifies the left edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
r (Right Offset) Specifies the right edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
t (Top Offset) Specifies the top edge of the rectangle.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_RelativeRect) is located in §A.4.1.
end note]
20.1.8.60 tint (Tint Effect)
This element specifies a tint effect. Shifts effect color values towards/away from hue by the specified amount.
Attributes Description
amt (Amount) Specifies by how much the color value is shifted.
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
hue (Hue) Specifies the hue towards which to tint.
The possible values for this attribute are defined by the ST_PositiveFixedAngle simple
type (§20.1.10.44).
[Note: The W3C XML Schema definition of this element’s content model (CT_TintEffect) is located in §A.4.1. end
note]
20.1.8.61 xfrm (Transform Effect)
This element specifies a transform effect. The transform is applied to each point in the shape's geometry using
the following matrix:
sx tan(kx) tx x
[tan(ky) sy ty]∙[y]
0 0 1 1
©ISO/IEC 2016 – All rights reserved 2883\n\n--- Page 2894 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
kx (Horizontal Specifies the horizontal skew angle, defined as the angle between the top-left corner and
Skew) bottom-left corner of the object's original bounding box. If positive, the bottom edge of
the shape is positioned to the right relative to the top edge.
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
ky (Vertical Skew) Specifies the vertical skew angle, defined as the angle between the top-left corner and
top-right corner of the object's original bounding box. If positive, the right edge of the
object is positioned lower relative to the left edge.
The possible values for this attribute are defined by the ST_FixedAngle simple type
(§20.1.10.23).
sx (Horizontal Ratio) Specifies a percentage by which to horizontally scale the object.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
sy (Vertical Ratio) Specifies a percentage by which to vertically scale the object.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
tx (Horizontal Shift) Specifies an amount by which to shift the object along the x-axis.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
ty (Vertical Shift) Specifies an amount by which to shift the object along the y-axis.
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_TransformEffect) is located in
§A.4.1. end note]
20.1.9 Shape Definitions and Attributes
The Shape Definitions and Attributes portion of the DrawingML framework deals with all geometric properties
for shapes within a document. This includes both preset geometries that publicly are interpreted by the
generating application and custom geometries that have their points and curves explicitly specified. In addition
to the underlying geometry of the shape there are also other coordinate-based properties for each shape that
this framework describes.
2884 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2895 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.9.1 ahLst (List of Shape Adjust Handles)
This element specifies the adjust handles that are applied to a custom geometry. These adjust handles specify
points within the geometric shape that can be used to perform certain transform operations on the shape.
[Example: Consider the scenario where a custom geometry, an arrow in this case, has been drawn and adjust
handles have been placed at the top left corner of both the arrow head and arrow body. The user interface can
then be made to transform only certain parts of the shape by using the corresponding adjust handle.
For instance if the user wished to change only the width of the arrow head then they would use the adjust
handle located on the top left of the arrow head. The result of adjusting this transforms the shape as shown
below.
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_AdjustHandleList) is located in
§A.4.1. end note]
20.1.9.2 ahPolar (Polar Adjust Handle)
This element specifies a polar adjust handle for a custom shape. The position of this adjust handle is specified by
the corresponding pos child element. The allowed adjustment of this adjust handle are specified via it's min and
max attributes. Based on the adjustment of this adjust handle certain corresponding guides are updated to
contain these values.
Attributes Description
gdRefAng (Angle Specifies the name of the guide that is updated with the adjustment angle from this
Adjustment Guide) adjust handle.
©ISO/IEC 2016 – All rights reserved 2885\n\n--- Page 2896 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_GeomGuideName simple
type (§20.1.10.28).
gdRefR (Radial Specifies the name of the guide that is updated with the adjustment radius from this
Adjustment Guide) adjust handle.
The possible values for this attribute are defined by the ST_GeomGuideName simple
type (§20.1.10.28).
maxAng (Maximum Specifies the maximum angle position that is allowed for this adjustment handle. If this
Angle Adjustment) attribute is omitted, then it is assumed that this adjust handle cannot move angularly.
That is the maxAng and minAng are equal.
The possible values for this attribute are defined by the ST_AdjAngle simple type
(§20.1.10.1).
maxR (Maximum Specifies the maximum radial position that is allowed for this adjustment handle. If this
Radial Adjustment) attribute is omitted, then it is assumed that this adjust handle cannot move radially. That
is the maxR and minR are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
minAng (Minimum Specifies the minimum angle position that is allowed for this adjustment handle. If this
Angle Adjustment) attribute is omitted, then it is assumed that this adjust handle cannot move angularly.
That is the maxAng and minAng are equal.
The possible values for this attribute are defined by the ST_AdjAngle simple type
(§20.1.10.1).
minR (Minimum Specifies the minimum radial position that is allowed for this adjustment handle. If this
Radial Adjustment) attribute is omitted, then it is assumed that this adjust handle cannot move radially. That
is the maxR and minR are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_PolarAdjustHandle) is located in
§A.4.1. end note]
20.1.9.3 ahXY (XY Adjust Handle)
This element specifies an XY-based adjust handle for a custom shape. The position of this adjust handle is
specified by the corresponding pos child element. The allowed adjustment of this adjust handle are specified via
it's min and max type attributes. Based on the adjustment of this adjust handle certain corresponding guides are
updated to contain these values.
2886 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2897 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
gdRefX (Horizontal Specifies the name of the guide that is updated with the adjustment x position from this
Adjustment Guide) adjust handle.
The possible values for this attribute are defined by the ST_GeomGuideName simple
type (§20.1.10.28).
gdRefY (Vertical Specifies the name of the guide that is updated with the adjustment y position from this
Adjustment Guide) adjust handle.
The possible values for this attribute are defined by the ST_GeomGuideName simple
type (§20.1.10.28).
maxX (Maximum Specifies the maximum horizontal position that is allowed for this adjustment handle. If
Horizontal this attribute is omitted, then it is assumed that this adjust handle cannot move in the x
Adjustment) direction. That is the maxX and minX are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
maxY (Maximum Specifies the maximum vertical position that is allowed for this adjustment handle. If this
Vertical attribute is omitted, then it is assumed that this adjust handle cannot move in the y
Adjustment) direction. That is the maxY and minY are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
minX (Minimum Specifies the minimum horizontal position that is allowed for this adjustment handle. If
Horizontal this attribute is omitted, then it is assumed that this adjust handle cannot move in the x
Adjustment) direction. That is the maxX and minX are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
minY (Minimum Specifies the minimum vertical position that is allowed for this adjustment handle. If this
Vertical attribute is omitted, then it is assumed that this adjust handle cannot move in the y
Adjustment) direction. That is the maxY and minY are equal.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_XYAdjustHandle) is located in
§A.4.1. end note]
20.1.9.4 arcTo (Draw Arc To)
This element specifies the existence of an arc within a shape path. It draws an arc with the specified parameters
from the current pen position to the new point specified. An arc is a line that is bent based on the shape of a
©ISO/IEC 2016 – All rights reserved 2887\n\n--- Page 2898 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
supposed circle. The length of this arc is determined by specifying both a start angle and an ending angle that
act together to effectively specify an end point for the arc.
[Example: The diagram shown below represents a single arc that has a start angle of 300 degrees and a swing
angle of 150 degrees. This arc is drawn using the supposed circle that is described using the hR and wR
attributes as shown below. The degrees by which the stAng must abide is shown along the circumference of the
circle. These degrees are to be specified in 60,000ths of a degree. If this arc were part of a shape the start angle
point along the circle would be the starting point along the path and the ending point would be the ending of
the angle swing along this supposed circle. That is any shape geometry coming before this arc in the shape path
would be joined with the upper point of this arc and consequently any geometry coming after this arc in the
path would be joined with the lower point of this arc.
end example]
Attributes Description
hR (Shape Arc This attribute specifies the height radius of the supposed circle being used to draw the
Height Radius) arc. This gives the circle a total height of (2 * hR). This total height could also be called
it's vertical diameter as it is the diameter for the y axis only.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
stAng (Shape Arc Specifies the start angle for an arc. This angle specifies what angle along the supposed
Start Angle) circle path is used as the start position for drawing the arc. This start angle is locked to
the last known pen position in the shape path. Thus guaranteeing a continuos shape
path.
The possible values for this attribute are defined by the ST_AdjAngle simple type
(§20.1.10.1).
swAng (Shape Arc Specifies the swing angle for an arc. This angle specifies how far angle-wise along the
Swing Angle) supposed cicle path the arc is extended. The extension from the start angle is always in
the clockwise direction around the supposed circle.
The possible values for this attribute are defined by the ST_AdjAngle simple type
(§20.1.10.1).
2888 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2899 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
wR (Shape Arc This attribute specifies the width radius of the supposed circle being used to draw the
Width Radius) arc. This gives the circle a total width of (2 * wR). This total width could also be called it's
horizontal diameter as it is the diameter for the x axis only.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DArcTo) is located in §A.4.1.
end note]
20.1.9.5 avLst (List of Shape Adjust Values)
This element specifies the adjust values that are applied to the specified shape. An adjust value is simply a guide
that has a value based formula specified. That is, no calculation takes place for an adjust value guide. Instead,
this guide specifies a parameter value that is used for calculations within the shape guides.
[Example: Consider the case where the user would like to specify a triangle with it's bottom edge defined not by
static points but by using a varying parameter, namely an adjust value. Consider the diagrams and DrawingML
shown below. This first triangle has been drawn with a bottom edge that is equal to the height, namely 2. Thus
we see in the figure below that the bottom of the triangle matches the bottom of the shape bounding box.
<a:xfrm>
<a:off x="3200400" y="1600200"/>
<a:ext cx="1705233" cy="679622"/>
</a:xfrm>
<a:custGeom>
<a:avLst>
<a:gd name="myGuide" fmla="val 2"/>
</a:avLst>
<a:gdLst/>
<a:ahLst/>
<a:cxnLst/>
<a:rect l="0" t="0" r="0" b="0"/>
©ISO/IEC 2016 – All rights reserved 2889\n\n--- Page 2900 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:pathLst>
<a:path w="2" h="2">
<a:moveTo>
<a:pt x="0" y="myGuide"/>
</a:moveTo>
<a:lnTo>
<a:pt x="2" y="myGuide"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
If however we change the adjust value to half that, namely 1. Then we see the entire bottom edge of the
triangle move to now be placed along the vertical midpoint within the shape bounding box. This is because both
of the bottom points in this triangle depend on this adjust value for their coordinate positions. The triangle and
corresponding DrawingML shown below illustrate this point.
<a:avLst>
<a:gd name="myGuide" fmla="val 1"/>
</a:avLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GeomGuideList) is located in
§A.4.1. end note]
20.1.9.6 close (Close Shape Path)
This element specifies the ending of a series of lines and curves in the creation path of a custom geometric
shape. When this element is encountered, the generating application should consider the corresponding path
closed. That is, any further lines or curves that follow this element should be ignored.
[Note: A path can be specified and not closed. A path such as this cannot however have any fill associated with it
as it has not been considered a closed geometric path. end note]
2890 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2901 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following DrawingML.
<a:custGeom>
<a:pathLst>
<a:path w="2824222" h="590309">
<a:moveTo>
<a:pt x="0" y="428263"/>
</a:moveTo>
<a:lnTo>
<a:pt x="1620455" y="590309"/>
</a:lnTo>
<a:lnTo>
<a:pt x="2824222" y="173620"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1562582" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
In the above example there is specified a four sided geometric shape that has all straight sides. While we only
see three lines being drawn via the lnTo element there are actually four sides because the last point of
(x=1562585, y=0) is connected to the first point in the creation path via a lnTo element. end example]
[Note: When the last point in the creation path does not meet with the first point in the creation path the
generating application should connect the last point with the first via a straight line, thus creating a closed shape
geometry. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DClose) is located in §A.4.1.
end note]
20.1.9.7 cubicBezTo (Draw Cubic Bezier Curve To)
This element specifies to draw a cubic bezier curve along the specified points. To specify a cubic bezier curve
there needs to be 3 points specified. The first two are control points used in the cubic bezier calculation and the
last is the ending point for the curve. The coordinate system used for this kind of curve is the path coordinate
system as this element is path specific.
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DCubicBezierTo) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2891\n\n--- Page 2902 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.9.8 custGeom (Custom Geometry)
This element specifies the existence of a custom geometric shape. This shape consists of a series of lines and
curves described within a creation path. In addition to this there can also be adjust values, guides, adjust
handles, connection sites and an inscribed rectangle specified for this custom geometric shape.
[Example: Consider the scenario when a preset geometry does not accurately depict what must be displayed in
the document. For this a custom geometry can be used to define most any 2-dimensional geometric shape.
Shown below is an example of such a custom geometry.
<a:custGeom>
<a:avLst/>
<a:gdLst/>
<a:ahLst/>
<a:cxnLst/>
<a:rect l="0" t="0" r="0" b="0"/>
<a:pathLst>
<a:path w="2650602" h="1261641">
<a:moveTo>
<a:pt x="0" y="1261641"/>
</a:moveTo>
<a:lnTo>
<a:pt x="2650602" y="1261641"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1226916" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
The custom geometry above is drawn by first moving to a specific starting point with the moveTo element. Then
a series of lnTo elements in the creation path specify the lines that make up the borders of the shape and finally
a close element is used to specify the end of the creation path. The resulting shape is shown above. end
example]
2892 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2903 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomGeometry2D) is located in
§A.4.1. end note]
20.1.9.9 cxn (Shape Connection Site)
This element specifies the existence of a connection site on a custom shape. A connection site allows a cxnSp to
be attached to this shape. This connection is maintained when the shape is repositioned within the document. It
should be noted that this connection is placed within the shape bounding box using the transform coordinate
system which is also called the shape coordinate system, as it encompasses the entire shape. The width and
height for this coordinate system are specified within the ext transform element.
[Note: The transform coordinate system is different from a path coordinate system as it is per shape instead of
per path within the shape. end note]
[Example: Consider the following custom geometry that has two connection sites specified. One connection is
located at the bottom left of the shape and the other at the bottom right. The following DrawingML would
describe such a custom geometry.
<a:xfrm>
<a:off x="3200400" y="1600200"/>
<a:ext cx="1705233" cy="679622"/>
</a:xfrm>
<a:custGeom>
<a:avLst/>
<a:gdLst/>
<a:ahLst/>
<a:cxnLst>
<a:cxn ang="0">
<a:pos x="0" y="679622"/>
</a:cxn>
<a:cxn ang="0">
<a:pos x="1705233" y="679622"/>
</a:cxn>
</a:cxnLst>
©ISO/IEC 2016 – All rights reserved 2893\n\n--- Page 2904 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:rect l="0" t="0" r="0" b="0"/>
<a:pathLst>
<a:path w="2" h="2">
<a:moveTo>
<a:pt x="0" y="2"/>
</a:moveTo>
<a:lnTo>
<a:pt x="2" y="2"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
end example]
Attributes Description
ang (Connection Specifies the incoming connector angle. This angle is the angle around the connection
Site Angle) site that an incoming connector tries to be routed to. This allows connectors to know
where the shape is in relation to the connection site and route connectors so as to avoid
any overlap with the shape.
[Example: Consider a simple square. In order to not have any connectors routed over the
shape, the collowing angles would be specified for their respective connection sites.
end example]
The possible values for this attribute are defined by the ST_AdjAngle simple type
(§20.1.10.1).
[Note: The W3C XML Schema definition of this element’s content model (CT_ConnectionSite) is located in
§A.4.1. end note]
2894 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2905 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.9.10 cxnLst (List of Shape Connection Sites)
This element specifies all the connection sites that are used for this shape. A connection site is specified by
defining a point within the shape bounding box that can have a cxnSp element attached to it. These connection
sites are specified using the shape coordinate system that is specified within the ext transform element.
[Note: The W3C XML Schema definition of this element’s content model (CT_ConnectionSiteList) is located in
§A.4.1. end note]
20.1.9.11 gd (Shape Guide)
This element specifies the precense of a shape guide that is used to govern the geometry of the specified shape.
A shape guide consists of a formula and a name that the result of the formula is assigned to. Recognized
formulas are listed with the fmla attribute documentation for this element.
[Note: The order in which guides are specified determines the order in which their values are calculated. For
instance it is not possible to specify a guide that uses another guides result when that guide has not yet been
calculated. end note]
[Example: Consider the case where the user would like to specify a triangle with it's bottom edge defined not by
static points but by using a varying parameter, namely an guide. Consider the diagrams and DrawingML shown
below. This first triangle has been drawn with a bottom edge that is equal to the 2/3 the value of the shape
height. Thus we see in the figure below that the triangle appears to occupy 2/3 of the vertical space within the
shape bounding box.
<a:xfrm>
<a:off x="3200400" y="1600200"/>
<a:ext cx="1705233" cy="679622"/>
</a:xfrm>
<a:custGeom>
<a:avLst/>
<a:gdLst>
<a:gd name="myGuide" fmla="*/ h 2 3"/>
</a:gdLst>
<a:ahLst/>
<a:cxnLst/>
<a:rect l="0" t="0" r="0" b="0"/>
<a:pathLst>
©ISO/IEC 2016 – All rights reserved 2895\n\n--- Page 2906 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:path w="1705233" h="679622">
<a:moveTo>
<a:pt x="0" y="myGuide"/>
</a:moveTo>
<a:lnTo>
<a:pt x="1705233" y="myGuide"/>
</a:lnTo>
<a:lnTo>
<a:pt x="852616" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
If however we change the guide to half that, namely 1/3. Then we see the entire bottom edge of the triangle
move to now only occupy 1/3 of the toal space within the shape bounding box. This is because both of the
bottom points in this triangle depend on this guide for their coordinate positions. The triangle and
corresponding DrawingML shown below illustrate this point.
<a:gdLst>
<a:gd name="myGuide" fmla="*/ h 1 3"/>
</a:gdLst>
end example]
Attributes Description
fmla (Shape Guide Specifies the formula that is used to calculate the value for a guide. Each formula has a
Formula) certain number of arguments and a specific set of operations to perform on these
arguments in order to generate a value for a guide. There are a total of 17 different
formulas available. These are shown below with the usage for each defined.
('*/') - Multiply Divide Formula
Arguments: 3 (fmla="*/ x y z")
Usage: "*/ x y z" = ((x * y) / z) = value of this guide
('+-') - Add Subtract Formula
Arguments: 3 (fmla="+- x y z")
Usage: "+- x y z" = ((x + y) - z) = value of this guide
2896 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2907 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
('+/') - Add Divide Formula
Arguments: 3 (fmla="+/ x y z")
Usage: "+/ x y z" = ((x + y) / z) = value of this guide
('?:') - If Else Formula
Arguments: 3 (fmla="?: x y z")
Usage: "?: x y z" = if (x > 0), then y = value of this guide,
else z = value of this guide
('abs') - Absolute Value Formula
Arguments: 1 (fmla="abs x")
Usage: "abs x" = if (x < 0), then (-1) * x = value of this guide
else x = value of this guide
('at2') - ArcTan Formula
Arguments: 2 (fmla="at2 x y")
Usage: "at2 x y" = arctan(y / x) = value of this guide
('cat2') - Cosine ArcTan Formula
Arguments: 3 (fmla="cat2 x y z")
Usage: "cat2 x y z" = (x*(cos(arctan(z / y))) = value of this guide
('cos') - Cosine Formula
Arguments: 2 (fmla="cos x y")
Usage: "cos x y" = (x * cos( y )) = value of this guide
('max') - Maximum Value Formula
Arguments: 2 (fmla="max x y")
Usage: "max x y" = if (x > y), then x = value of this guide
else y = value of this guide
('min') - Minimum Value Formula
Arguments: 2 (fmla="min x y")
Usage: "min x y" = if (x < y), then x = value of this guide
else y = value of this guide
('mod') - Modulo Formula
Arguments: 3 (fmla="mod x y z")
Usage: "mod x y z" = sqrt(x^2 + b^2 + c^2) = value of this guide
('pin') - Pin To Formula
Arguments: 3 (fmla="pin x y z")
Usage: "pin x y z" = if (y < x), then x = value of this guide
else if (y > z), then z = value of this guide
else y = value of this guide
('sat2') - Sine ArcTan Formula
Arguments: 3 (fmla="sat2 x y z")
Usage: "sat2 x y z" = (x*sin(arctan(z / y))) = value of this guide
('sin') - Sine Formula
Arguments: 2 (fmla="sin x y")
©ISO/IEC 2016 – All rights reserved 2897\n\n--- Page 2908 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Usage: "sin x y" = (x * sin( y )) = value of this guide
('sqrt') - Square Root Formula
Arguments: 1 (fmla="sqrt x")
Usage: "sqrt x" = sqrt(x) = value of this guide
('tan') - Tangent Formula
Arguments: 2 (fmla="tan x y")
Usage: "tan x y" = (x * tan( y )) = value of this guide
('val') - Literal Value Formula
Arguments: 1 (fmla="val x")
Usage: "val x" = x = value of this guide
[Note: Guides that have a literal value formula specified via fmla="val x" above should
only be used within the avLst as an adjust value for the shape. This however is not
strictly enforced. end note]
The possible values for this attribute are defined by the ST_GeomGuideFormula simple
type (§20.1.10.27).
name (Shape Guide Specifies the name that is used to reference to this guide. This name can be used just as a
Name) variable would within an equation. That is this name can be substituted for literal values
within other guides or the specification of the shape path.
The possible values for this attribute are defined by the ST_GeomGuideName simple
type (§20.1.10.28).
[Note: The W3C XML Schema definition of this element’s content model (CT_GeomGuide) is located in §A.4.1.
end note]
20.1.9.12 gdLst (List of Shape Guides)
This element specifies all the guides that are used for this shape. A guide is specified by the gd element and
defines a calculated value that can be used for the construction of the corresponding shape.
[Note: Guides that have a literal value formula specified via fmla="val x" above should only be used within the
avLst as an adjust value for the shape. This however is not strictly enforced. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_GeomGuideList) is located in
§A.4.1. end note]
20.1.9.13 lnTo (Draw Line To)
This element specifies the drawing of a straight line from the current pen position to the new point specified.
This line becomes part of the shape geometry, representing a side of the shape. The coordinate system used
when specifying this line is the path coordinate system.
2898 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2909 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DLineTo) is located in §A.4.1.
end note]
20.1.9.14 moveTo (Move Path To)
This element specifies a set of new coordinates to move the shape cursor to. This element is only used for
drawing a custom geometry. When this element is utilized the pt element is used to specify a new set of shape
coordinates that the shape cursor should be moved to. This does not draw a line or curve to this new position
from the old position but simply move the cursor to a new starting position. It is only when a path drawing
element such as lnTo is used that a portion of the path is drawn.
[Example: Consider the case where a user wishes to begin drawing a custom geometry not at the default starting
coordinates of x=0 , y=0 but at coordinates further inset into the shape coordinate space. The following
DrawingML would specify such a case.
<a:custGeom>
<a:pathLst>
<a:path w="2824222" h="590309">
<a:moveTo>
<a:pt x="0" y="428263"/>
</a:moveTo>
<a:lnTo>
<a:pt x="1620455" y="590309"/>
</a:lnTo>
<a:lnTo>
<a:pt x="2824222" y="173620"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1562582" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
Notice the moveTo element advances the y coordinates before any actual lines are drawn. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DMoveTo) is located in
§A.4.1. end note]
20.1.9.15 path (Shape Path)
This element specifies a creation path consisting of a series of moves, lines and curves that when combined
forms a geometric shape. This element is only utilized if a custom geometry is specified.
©ISO/IEC 2016 – All rights reserved 2899\n\n--- Page 2910 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: Since multiple paths are allowed the rules for drawing are that the path specified later in the pathLst is
drawn on top of all previous paths. end note]
[Example: Consider the following DrawingML.
<a:custGeom>
<a:pathLst>
<a:path w="2824222" h="590309">
<a:moveTo>
<a:pt x="0" y="428263"/>
</a:moveTo>
<a:lnTo>
<a:pt x="1620455" y="590309"/>
</a:lnTo>
<a:lnTo>
<a:pt x="2824222" y="173620"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1562582" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
In the above example there is specified a four sided geometric shape that has all straight sides. While we only
see three lines being drawn via the lnTo element there are actually four sides because the last point of
(x=1562585, y=0) is connected to the first point in the creation path via a lnTo element. end example]
Attributes Description
extrusionOk (3D Specifies that the use of 3D extrusions are possible on this path. This allows the
Extrusion Allowed) generating application to know whether 3D extrusion can be applied in any form. If this
attribute is omitted then a value of 0, or false is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
fill (Path Fill) Specifies how the corresponding path should be filled. If this attribute is omitted, a value
of "norm" is assumed.
The possible values for this attribute are defined by the ST_PathFillMode simple type
(§20.1.10.37).
h (Path Height) Specifies the height, or maximum y coordinate that should be used for within the path
coordinate system. This value determines the vertical placement of all points within the
corresponding path as they are all calculated using this height attribute as the max y
2900 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2911 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
coordinate.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
stroke (Path Stroke) Specifies if the corresponding path should have a path stroke shown. This is a boolean
value that affect the outline of the path. If this attribute is omitted, a value of true is
assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
w (Path Width) Specifies the width, or maximum x coordinate that should be used for within the path
coordinate system. This value determines the horizontal placement of all points within
the corresponding path as they are all calculated using this width attribute as the max x
coordinate.
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2D) is located in §A.4.1. end
note]
20.1.9.16 pathLst (List of Shape Paths)
This element specifies the entire path that is to make up a single geometric shape. The pathLst can consist of
many individual paths within it.
[Example: Consider the following DrawingML.
<a:custGeom>
<a:pathLst>
<a:path w="2824222" h="590309">
<a:moveTo>
<a:pt x="0" y="428263"/>
</a:moveTo>
<a:lnTo>
<a:pt x="1620455" y="590309"/>
</a:lnTo>
<a:lnTo>
<a:pt x="2824222" y="173620"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1562582" y="0"/>
</a:lnTo>
©ISO/IEC 2016 – All rights reserved 2901\n\n--- Page 2912 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
In the above example there is specified a four sided geometric shape that has all straight sides. While we only
see three lines being drawn via the lnTo element there are actually four sides because the last point of
(x=1562585, y=0) is connected to the first point in the creation path via a lnTo element. end example]
[Note: A geometry with multiple paths within it should be treated visually as if each path were a distinct shape.
That is each creation path has its first point and last point joined to form a closed shape. However, the
generating application should then connect the last point to the first point of the new shape. If a close element
is encountered at the end of the previous creation path then this joining line should not be rendered by the
generating application. The rendering should resume with the first line or curve on the new creation path. end
note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DList) is located in §A.4.1. end
note]
20.1.9.17 pos (Shape Position Coordinate)
Specifies a position coordinate within the shape bounding box. It should be noted that this coordinate is placed
within the shape bounding box using the transform coordinate system which is also called the shape coordinate
system, as it encompasses the entire shape. The width and height for this coordinate system are specified within
the ext transform element.
[Note: When specifying a point coordinate in path coordinate space it should be noted that the top left of the
coordinate space is x=0, y=0 and the coordinate points for x grow to the right and for y grow down. This is
illustrated in the diagram below.
end note]
2902 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2913 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: To highlight the differences in the coordinate systems consider the drawing of the following triangle.
Notice that the dimensions of the triangle are specified using the shape coordinate system with EMUs as the
units via the ext transform element. Thus we see this shape is 1705233 EMUs wide by 679622 EMUs tall.
However when looking at how the path for this shape is drawn we see that the x and y values fall between 0 and
2. This is because the path coordinate system has the arbitrary dimensions of 2 for the width and 2 for the
height. Thus we see that a y coordinate of 2 within the path coordinate system specifies a y coordinate of
679622 within the shape coordinate system for this particular case.
<a:xfrm>
<a:off x="3200400" y="1600200"/>
<a:ext cx="1705233" cy="679622"/>
</a:xfrm>
<a:custGeom>
<a:avLst/>
<a:gdLst/>
<a:ahLst/>
<a:cxnLst/>
<a:rect l="0" t="0" r="0" b="0"/>
<a:pathLst>
<a:path w="2" h="2">
<a:moveTo>
<a:pt x="0" y="2"/>
</a:moveTo>
<a:lnTo>
<a:pt x="2" y="2"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
end example]
©ISO/IEC 2016 – All rights reserved 2903\n\n--- Page 2914 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
x (X-Coordinate) Specifies the x coordinate for this position coordinate. The units for this coordinate space
are defined by the width of the path coordinate system. This coordinate system is
overlayed on top of the shape coordinate system thus occupying the entire shape
bounding box. Because the units for within this coordinate space are determined by the
path width and height an exact measurement unit cannot be specified here.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
y (Y-Coordinate) Specifies the y coordinate for this position coordinate. The units for this coordinate space
are defined by the height of the path coordinate system. This coordinate system is
overlayed on top of the shape coordinate system thus occupying the entire shape
bounding box. Because the units for within this coordinate space are determined by the
path width and height an exact measurement unit cannot be specified here.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_AdjPoint2D) is located in §A.4.1.
end note]
20.1.9.18 prstGeom (Preset geometry)
This element specifies when a preset geometric shape should be used instead of a custom geometric shape. The
generating application should be able to render all preset geometries enumerated in the ST_ShapeType list.
[Example: Consider the scenario when a user does not wish to specify all the lines and curves that make up the
desired shape but instead chooses to use a preset geometry. The following DrawingML would specify such a
case.
<p:sp>
<p:nvSpPr>
<p:cNvPr id="4" name="My Preset Shape"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
<p:spPr>
<a:xfrm>
<a:off x="1981200" y="533400"/>
<a:ext cx="1143000" cy="1066800"/>
</a:xfrm>
<a:prstGeom prst="heart">
</a:prstGeom>
</p:spPr>
</p:sp>
2904 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2915 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The output shape rendered by this DrawingML is shown above. end example]
Attributes Description
prst (Preset Shape) Specifies the preset geometry that is used for this shape. This preset can have any of the
values in the enumerated list for ST_ShapeType. This attribute is required in order for a
preset geometry to be rendered.
[Example: Consider the sample DrawingML below.
<p:sp>
<p:nvSpPr>
<p:cNvPr id="4" name="Sun 3"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
<p:spPr>
<a:xfrm>
<a:off x="1981200" y="533400"/>
<a:ext cx="1143000" cy="1066800"/>
</a:xfrm>
<a:prstGeom prst="sun">
</a:prstGeom>
</p:spPr>
</p:sp>
In the above example a preset geometry has been used to define a shape. The shape
utilized here is the sun shape. end example]
The possible values for this attribute are defined by the ST_ShapeType simple type
(§20.1.10.56).
[Note: The W3C XML Schema definition of this element’s content model (CT_PresetGeometry2D) is located in
§A.4.1. end note]
20.1.9.19 prstTxWarp (Preset Text Warp)
This element specifies when a preset geometric shape should be used to transform a piece of text. This
operation is known formally as a text warp. The generating application should be able to render all preset
geometries enumerated in the ST_TextShapeType list.
©ISO/IEC 2016 – All rights reserved 2905\n\n--- Page 2916 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the case where the user wishes to accent a piece of text by warping it's shape. For this to
occur a preset shape is chosen from the ST_TextShapeType list and applied to the entire body of text.
<p:sp>
<p:txBody>
<a:bodyPr wrap="none" rtlCol="0">
<a:prstTxWarp prst="textInflate">
</a:prstTxWarp>
<a:spAutoFit/>
</a:bodyPr>
<a:lstStyle/>
<a:p>
…
<a:t>Sample Text</a:t>
…
</a:p>
</p:txBody>
</p:sp>
The resulting text that has now had the Inflate text warp applied to it is shown above. end example]
Using any of the presets listed under the ST_TextShapeType list below it is possible to apply a text warp to a run
of DrawingML text via the following steps.
If you look at any of the text warps in the file format you notice that each consists of two paths. This
corresponds to a top path (first one specified) and a bottom path (second one specified). Now the top path and
the bottom path represent the top line and base line that the text needs to be warped to. This is done in the
following way:
1. Compute the rectangle that the unwarped text resides in. (tightest possible rectangle around text, no
white space except for “space characters”)
2. Take each of the quadratic and cubic Bezier curves that are used to calculate the original character and
change their end points and control points by the following method…
3. Move a vertical line horizontally along the original text rectangle and find the horizontal percentage that
a given end point or control point lives at. (.5 for the middle for instance)
4. Now do the same thing for this point vertically. Find the vertical percentage that this point lives at with
the top and bottom of this text rectangle being the respective top and bottom bounds. (0.0 and 1.0
respectively)
2906 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2917 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
5. Now that we have the percentages for a given point in a Bezier equation we can map that to the new
point in the warped text environment.
6. Going back to the top and bottom paths specified in the file format we can take these and flatten them
out to a straight arc (top and bottom might be different lengths)
7. After they are straight we can measure them both horizontally to find the same percentage point that
we found within the original text rectangle. (0.5 let’s say)
8. So then we measure 50% along the top path and 50% along the bottom path, putting the paths back to
their original curvy shapes.
9. Once we have these two points we can draw a line between them that serves as our vertical line in the
original text rectangle [Note: This might not be truly vertical as 50% on the top does not always line up
with 50% on the bottom. end note]
10. Taking this new line we then follow it from top to bottom the vertical percentage amount that we got
from step 4.
11. This is then the new point that should be used in place of the old point in the original text rectangle.
12. We then continue doing these same steps for each of the end points and control points within the body
of text. (is applied to a whole body of text only)
[Note: Horizxontal percentages begin at 0.0 and continue to 1.0, left to right. Vertical percentages begin at 0.0
and continue to 1.0, top to bottom. end note]
[Note: Since this is a shape it does have both a shape coordinate system and a path coordinate system. end note]
Attributes Description
prst (Preset Warp Specifies the preset geometry that is used for a shape warp on a piece of text. This preset
Shape) can have any of the values in the enumerated list for ST_TextShapeType. This attribute
is required in order for a text warp to be rendered.
[Example: Consider the sample DrawingML below.
<p:sp>
<p:txBody>
<a:bodyPr wrap="none" rtlCol="0">
<a:prstTxWarp prst="textInflate">
</a:prstTxWarp>
<a:spAutoFit/>
</a:bodyPr>
<a:lstStyle/>
<a:p>
…
<a:t>Sample Text</a:t>
…
</a:p>
</p:txBody>
</p:sp>
In the above example a preset text shape geometry has been used to define the warping
©ISO/IEC 2016 – All rights reserved 2907\n\n--- Page 2918 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
shape. The shape utilized here is the sun shape. end example]
The possible values for this attribute are defined by the ST_TextShapeType simple type
(§20.1.10.76).
[Note: The W3C XML Schema definition of this element’s content model (CT_PresetTextShape) is located in
§A.4.1. end note]
20.1.9.20 pt (Shape Path Point)
This element specifies an x-y coordinate within the path coordinate space. This coordinate space is determined
by the width and height attributes defined within the path element. A point is utilized by one of it's parent
elements to specify the next point of interest in custom geometry shape. Depending on the parent element used
the point can either have a line drawn to it or the cursor can simply be moved to this new location.
[Note: When specifying a point coordinate in path coordinate space it should be noted that the top left of the
coordinate space is x=0, y=0 and the coordinate points for x grow to the right and for y grow down. This is
illustrated in the diagram below.
end note]
Specifies a position coordinate within the shape bounding box. It should be noted that this coordinate is placed
within the shape bounding box using the transform coordinate system which is also called the shape coordinate
system, as it encompasses the entire shape. The width and height for this coordinate system are specified within
the ext transform element.
[Example: To highlight the differences in the coordinate systems consider the drawing of the following triangle.
Notice that the dimensions of the triangle are specified using the shape coordinate system with EMUs as the
units via the ext transform element. Thus we see this shape is 1705233 EMUs wide by 679622 EMUs tall.
However when looking at how the path for this shape is drawn we see that the x and y values fall between 0 and
2908 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2919 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
2. This is because the path coordinate system has the arbitrary dimensions of 2 for the width and 2 for the
height. Thus we see that a y coordinate of 2 within the path coordinate system specifies a y coordinate of
679622 within the shape coordinate system for this particular case.
<a:xfrm>
<a:off x="3200400" y="1600200"/>
<a:ext cx="1705233" cy="679622"/>
</a:xfrm>
<a:custGeom>
<a:avLst/>
<a:gdLst/>
<a:ahLst/>
<a:cxnLst/>
<a:rect l="0" t="0" r="0" b="0"/>
<a:pathLst>
<a:path w="2" h="2">
<a:moveTo>
<a:pt x="0" y="2"/>
</a:moveTo>
<a:lnTo>
<a:pt x="2" y="2"/>
</a:lnTo>
<a:lnTo>
<a:pt x="1" y="0"/>
</a:lnTo>
<a:close/>
</a:path>
</a:pathLst>
</a:custGeom>
end example]
Attributes Description
x (X-Coordinate) Specifies the x coordinate for this position coordinate. The units for this coordinate space
are defined by the width of the path coordinate system. This coordinate system is
overlayed on top of the shape coordinate system thus occupying the entire shape
bounding box. Because the units for within this coordinate space are determined by the
path width and height an exact measurement unit cannot be specified here.
©ISO/IEC 2016 – All rights reserved 2909\n\n--- Page 2920 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
y (Y-Coordinate) Specifies the y coordinate for this position coordinate. The units for this coordinate space
are defined by the height of the path coordinate system. This coordinate system is
overlayed on top of the shape coordinate system thus occupying the entire shape
bounding box. Because the units for within this coordinate space are determined by the
path width and height an exact measurement unit cannot be specified here.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_AdjPoint2D) is located in §A.4.1.
end note]
20.1.9.21 quadBezTo (Draw Quadratic Bezier Curve To)
This element specifies to draw a quadratic bezier curve along the specified points. To specify a quadratic bezier
curve there needs to be 2 points specified. The first is a control point used in the quadratic bezier calculation
and the last is the ending point for the curve. The coordinate system used for this type of curve is the path
coordinate system as this element is path specific.
[Note: The W3C XML Schema definition of this element’s content model (CT_Path2DQuadBezierTo) is located in
§A.4.1. end note]
20.1.9.22 rect (Shape Text Rectangle)
This element specifies the rectangular bounding box for text within a custGeom shape. The default for this
rectangle is the bounding box for the shape. This can be modified using this elements four attributes to inset or
extend the text bounding box.
[Note: Text specified to reside within this shape text rectangle can flow outside this bounding box. Depending on
the autofit options within the txBody element the text might not entirely reside within this shape text rectangle.
end note]
Attributes Description
b (Bottom Position) Specifies the y coordinate of the bottom edge for a shape text rectangle. The units for
this edge is specified in EMUs as the positioning here is based on the shape coordinate
system. The width and height for this coordinate system are specified within the ext
transform element.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
l (Left) Specifies the x coordinate of the left edge for a shape text rectangle. The units for this
2910 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2921 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
edge is specified in EMUs as the positioning here is based on the shape coordinate
system. The width and height for this coordinate system are specified within the ext
transform element.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
r (Right) Specifies the x coordinate of the right edge for a shape text rectangle. The units for this
edge is specified in EMUs as the positioning here is based on the shape coordinate
system. The width and height for this coordinate system are specified within the ext
transform element.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
t (Top) Specifies the y coordinate of the top edge for a shape text rectangle. The units for this
edge is specified in EMUs as the positioning here is based on the shape coordinate
system. The width and height for this coordinate system are specified within the ext
transform element.
The possible values for this attribute are defined by the ST_AdjCoordinate simple type
(§20.1.10.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_GeomRect) is located in §A.4.1. end
note]
20.1.10 Simple Types
This is the complete list of simple types dedicated to DrawingML framework.
20.1.10.1 ST_AdjAngle (Adjustable Angle Methods)
This simple type is an adjustable angle, either an absolute angle or a reference to a geometry guide. The units
for an adjustable angle are 60,000ths of a degree.
This simple type is a union of the following types:
 The ST_Angle simple type (§20.1.10.3).
 The ST_GeomGuideName simple type (§20.1.10.28).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AdjAngle) is located in §A.4.1.
end note]
20.1.10.2 ST_AdjCoordinate (Adjustable Coordinate Methods)
This simple type is an adjustable coordinate is either an absolute coordinate position or a reference to a
geometry guide.
©ISO/IEC 2016 – All rights reserved 2911\n\n--- Page 2922 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is a union of the following types:
 The ST_Coordinate simple type (§20.1.10.16).
 The ST_GeomGuideName simple type (§20.1.10.28).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AdjCoordinate) is located in
§A.4.1. end note]
20.1.10.3 ST_Angle (Angle)
This simple type represents an angle in 60,000ths of a degree. Positive angles are clockwise (i.e., towards the
positive y axis); negative angles are counter-clockwise (i.e., towards the negative y axis).
This simple type's contents are a restriction of the W3C XML Schema int datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Angle) is located in §A.4.1. end
note]
20.1.10.4 ST_AnimationBuildType (Animation Build Type)
This simple type specifies the ways that an animation can be built, or animated.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allAtOnce (Animate At Once) Animate all objects as one.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AnimationBuildType) is located
in §A.4.1. end note]
20.1.10.5 ST_AnimationChartBuildType (Chart Animation Build Type)
This simple type specifies the ways that a chart animation can be built. That is, it specifies the way in which the
objects within the chart should be animated.
This simple type is a union of the following types:
 The ST_AnimationBuildType simple type (§20.1.10.4).
 The ST_AnimationChartOnlyBuildType simple type (§20.1.10.6).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AnimationChartBuildType) is
located in §A.4.1. end note]
20.1.10.6 ST_AnimationChartOnlyBuildType (Chart only Animation Types)
This simple type specifies the build options available only for animating a chart. These options specify the
manner in which the objects within the chart should be grouped and animated.
2912 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2923 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
category (Catefory) Animate by each category
categoryEl (Category Element) Animate by each element within the category
series (Series) Animate by each series.
seriesEl (Series Element) Animate by each element within the series
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AnimationChartOnlyBuildType)
is located in §A.4.1. end note]
20.1.10.7 ST_AnimationDgmBuildType (Diagram Animation Build Type)
This simple type specifies the ways that a diagram animation can be built. That is, it specifies the way in which
the objects within the diagram graphical object should be animated.
This simple type is a union of the following types:
 The ST_AnimationBuildType simple type (§20.1.10.4).
 The ST_AnimationDgmOnlyBuildType simple type (§20.1.10.8).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AnimationDgmBuildType) is
located in §A.4.1. end note]
20.1.10.8 ST_AnimationDgmOnlyBuildType (Diagram only Animation Types)
This simple type specifies the build options available only for animating a diagram. These options specify the
manner in which the objects within the chart should be grouped and animated.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
lvlAtOnce (Each Level at Once) Animate the diagram one level at a time, animating
the whole level as one object
lvlOne (Level One-by-One) Animate the diagram by the elements within a level,
animating them one level element at a time.
one (Elements One-by-One) Animate the diagram by elements. For a tree diagram
the animation occurs by branch within the diagram
tree.
©ISO/IEC 2016 – All rights reserved 2913\n\n--- Page 2924 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AnimationDgmOnlyBuildType) is
located in §A.4.1. end note]
20.1.10.9 ST_BevelPresetType (Bevel Presets)
Represents a preset for a type of bevel which can be applied to a shape in 3D. The bevel properties are applied
differently depending on the type of bevel defined for a shape.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
angle (Angle) [Example: Consider the following example of an
angle bevel type applied to a shape:
end example]
artDeco (Art Deco) [Example: Consider the following example of an
artDeco bevel type applied to a shape:
end example]
circle (Circle) [Example: Consider the following example of an
circle bevel type applied to a shape:
2914 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2925 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
convex (Convex) [Example: Consider the following example of an
convex bevel type applied to a shape:
end example]
coolSlant (Cool Slant) [Example: Consider the following example of an
coolSlant bevel type applied to a shape:
end example]
cross (Cross) [Example: Consider the following example of an
cross bevel type applied to a shape:
©ISO/IEC 2016 – All rights reserved 2915\n\n--- Page 2926 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
divot (Divot) [Example: Consider the following example of an
divot bevel type applied to a shape:
end example]
hardEdge (Hard Edge) [Example: Consider the following example of an
hardEdge bevel type applied to a shape:
end example]
relaxedInset (Relaxed Inset) [Example: Consider the following example of an
2916 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2927 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
relaxedInset bevel type applied to a shape:
end example]
riblet (Riblet) [Example: Consider the following example of an
riblet bevel type applied to a shape:
end example]
slope (Slope) [Example: Consider the following example of an
slope bevel type applied to a shape:
end example]
©ISO/IEC 2016 – All rights reserved 2917\n\n--- Page 2928 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
softRound (Soft Round) [Example: Consider the following example of an
softRound bevel type applied to a shape:
end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_BevelPresetType) is located in
§A.4.1. end note]
20.1.10.10 ST_BlackWhiteMode (Black and White Mode)
This simple type specifies how an object should be rendered when specified to be in black and white mode.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
auto (Automatic) Object rendered with automatic coloring
black (Black) Object rendered with black-only coloring
blackGray (Black and Gray) Object rendered with black and gray coloring
blackWhite (Black and White) Object rendered within black and white coloring
clr (Color) Object rendered with normal coloring
gray (Gray) Object rendered with gray coloring
grayWhite (Gray and White) Object rendered within gray and white coloring
hidden (Hidden) Object rendered with hidden coloring
invGray (Inverse Gray) Object rendered with inverse gray coloring
ltGray (Light Gray) Object rendered with light gray coloring
white (White) Object rendered within white coloirng
2918 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2929 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_BlackWhiteMode) is located in
§A.4.1. end note]
20.1.10.11 ST_BlendMode (Blend Mode)
This simple type describes how to render effects one on top of another.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
darken (Darken) Darken
lighten (Lighten) Lighten
mult (Multiply) Multiply
over (Overlay) Overlay
screen (Screen) Screen
[Note: The W3C XML Schema definition of this simple type’s content model (ST_BlendMode) is located in §A.4.1.
end note]
20.1.10.12 ST_BlipCompression (Blip Compression Type)
This type specifies the amount of compression that has been used for a particular binary large image or picture
(blip).
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
email (Email Compression) Compression size suitable for inclusion with email
hqprint (High Quality Printing Compression) Compression size suitable for high quality printing
none (No Compression) No compression was used
print (Printing Compression) Compression size suitable for printing
screen (Screen Viewing Compression) Compression size suitable for viewing on screen
[Note: The W3C XML Schema definition of this simple type’s content model (ST_BlipCompression) is located in
§A.4.1. end note]
20.1.10.13 ST_ChartBuildStep (Chart Animation Build Step)
This simple type specifies an animation build step within a chart animation.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 2919\n\n--- Page 2930 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allPts (All Points) Animate all points within the chart for this animation
build step
category (Category) Animate a chart category for this animation build step
gridLegend (Grid and Legend) Animate the chart grid and legend for this animation
build step
ptInCategory (Category Points) Animate a point in a chart category for this animation
build step
ptInSeries (Series Points) Animate a point in a chart series for this animation
build step
series (Series) Animate a chart series for this animation build step
[Note: The W3C XML Schema definition of this simple type’s content model (ST_ChartBuildStep) is located in
§A.4.1. end note]
20.1.10.14 ST_ColorSchemeIndex (Theme Color Reference)
A reference to a color in the color scheme.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
accent1 (Accent 1) Represents the accent 1 color.
accent2 (Accent 2) Represents the accent 2 color.
accent3 (Accent 3) Represents the accent 3 color.
accent4 (Accent 4) Represents the accent 4 color.
accent5 (Accent 5) Represents the accent 5 color.
accent6 (Accent 6) Represents the accent 6 color.
dk1 (Dark 1) Represents the first dark color.
dk2 (Dark 2) Represents the second dark color.
folHlink (Followed Hyperlink) Represents the followed hyperlink color.
hlink (Hyperlink) Represents the hyperlink color.
lt1 (Light 1) Represents the first light color.
lt2 (Light 2) Represents the second light color.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_ColorSchemeIndex) is located in
§A.4.1. end note]
2920 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2931 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.15 ST_CompoundLine (Compound Line Type)
This simple type specifies the compound line type that is to be used for lines with text such as underlines.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
dbl (Double Lines) Double lines of equal width
sng (Single Line) Single line: one normal width
thickThin (Thick Thin Double Lines) Double lines: one thick, one thin
thinThick (Thin Thick Double Lines) Double lines: one thin, one thick
tri (Thin Thick Thin Triple Lines) Three lines: thin, thick, thin
[Note: The W3C XML Schema definition of this simple type’s content model (ST_CompoundLine) is located in
§A.4.1. end note]
20.1.10.16 ST_Coordinate (Coordinate)
This simple type represents a one dimensional position or length as either:
 EMUs.
 A number followed immediately by a unit identifier.
This simple type is a union of the following types:
 The ST_CoordinateUnqualified simple type (§20.1.10.19).
 The ST_UniversalMeasure simple type (§22.9.2.15).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Coordinate) is located in §A.4.1.
end note]
20.1.10.17 ST_Coordinate32 (Coordinate Point)
This simple type specifies a coordinate within the document. This can be used for measurements or spacing; its
maximum size is 2147483647 EMUs.
Its contents can contain either:
 A whole number, whose contents consist of a measurement in EMUs (English Metric Units)
 A number immediately followed by a unit identifier
This simple type is a union of the following types:
 The ST_Coordinate32Unqualified simple type (§20.1.10.18).
 The ST_UniversalMeasure simple type (§22.9.2.15).
©ISO/IEC 2016 – All rights reserved 2921\n\n--- Page 2932 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Coordinate32) is located in
§A.4.1. end note]
20.1.10.18 ST_Coordinate32Unqualified (Coordinate Point)
This simple type specifies a coordinate within the document. This can be used for measurements or spacing with
the maximum size requirement being a 32 bit integer.
The units of measurement used here are EMUs (English Metric Units).
This simple type's contents are a restriction of the W3C XML Schema int datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Coordinate32Unqualified) is
located in §A.4.1. end note]
20.1.10.19 ST_CoordinateUnqualified (Coordinate)
This simple type represents a one dimensional position or length in EMUs.
This simple type's contents are a restriction of the W3C XML Schema long datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to -27273042329600.
 This simple type has a maximum value of less than or equal to 27273042316900.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_CoordinateUnqualified) is
located in §A.4.1. end note]
20.1.10.20 ST_DgmBuildStep (Diagram Animation Build Steps)
This simple type specifies an animation build step within a diagram animation.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bg (Background) Animate the diagram background for this animation
build step
sp (Shape) Animate a diagram shape for this animation build step
[Note: The W3C XML Schema definition of this simple type’s content model (ST_DgmBuildStep) is located in
§A.4.1. end note]
20.1.10.21 ST_DrawingElementId (Drawing Element ID)
This simple type specifies a unique integer identifier for each drawing element.
2922 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2933 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_DrawingElementId) is located in
§A.4.1. end note]
20.1.10.22 ST_EffectContainerType (Effect Container Type)
This simple type determines the relationship between effects in a container, either sibling or tree.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
sib (Sibling) Each effect is separately applied to the parent object.
[Example: If the parent element contains an outer
shadow and a reflection, the resulting effect is a
shadow around the parent object and a reflection of
the object. The reflection does not have a shadow.
end example]
tree (Tree) Each effect is applied to the result of the previous
effect.
[Example: If the parent element contains an outer
shadow followed by a glow, the shadow is first applied
to the parent object. Then, the glow is applied to the
shadow (rather than the original object). The resulting
effect would be a glowing shadow. end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_EffectContainerType) is located
in §A.4.1. end note]
20.1.10.23 ST_FixedAngle (Fixed Angle)
This simple type represents a fixed range angle in 60000ths of a degree. Range from (-90, 90 degrees).
This simple type's contents are a restriction of the ST_Angle datatype (§20.1.10.3).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than -5400000.
 This simple type has a maximum value of less than 5400000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_FixedAngle) is located in §A.4.1.
end note]
©ISO/IEC 2016 – All rights reserved 2923\n\n--- Page 2934 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.24 ST_FixedPercentage (Fixed Percentage)
This simple type represents a fixed percentage from negative one hundred to positive one hundred percent. See
the union's member types for details.
This simple type is a union of the following types:
 The ST_FixedPercentage simple type (§22.9.2.3).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_FixedPercentage) is located in
§A.4.1. end note]
20.1.10.25 ST_FontCollectionIndex (Font Collection Index)
This simple type represents one of the fonts associated with the style.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
major (Major Font) The major font of the style's font scheme.
minor (Minor Font) The minor font of the style's font scheme.
none (None) No font reference.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_FontCollectionIndex) is located
in §A.4.1. end note]
20.1.10.26 ST_FOVAngle (Field of View Angle)
Represents a positive angle in 60000ths of a degree. Range from [0, 180] degrees.
This simple type's contents are a restriction of the ST_Angle datatype (§20.1.10.3).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 10800000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_FOVAngle) is located in §A.4.1.
end note]
20.1.10.27 ST_GeomGuideFormula (Geometry Guide Formula Properties)
This simple type specifies a geometry guide formula.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
2924 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2935 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_GeomGuideFormula) is located
in §A.4.1. end note]
20.1.10.28 ST_GeomGuideName (Geometry Guide Name Properties)
This simple type specifies a geometry guide name.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_GeomGuideName) is located in
§A.4.1. end note]
20.1.10.29 ST_LightRigDirection (Light Rig Direction)
Represents the direction from which the light rig is positioned relative to the scene. The light rig, itself, can be
made up of multiple lights in any orientation around a given shape. This simple type defines the orientation of
the light rig as a whole, and not the individual lights within the rig. This means that because the direction of the
light rig is left, that does not guarantee the light is coming from the left side of the shape, but rather the
orientation of the rig as a whole is rotated to the left.
[Example: Consider the following example as a visual representation of a light rig oriented from the top of the
shape in the center:
In this example we see that the light rig defines three lights (all in a single plane as represented by the black
circular line). The lights defined in this representation can all have different intensities, which means, for this
example, Light 3 and Light 2 look to have a more intense effect (or could even be a different color) than Light 1.
One can imagine rotating this rig to the so that Light 1 is to the right of the shape when the light rig direction is
defined to be right. end example]
©ISO/IEC 2016 – All rights reserved 2925\n\n--- Page 2936 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The following properties were used to define the shape used in the image examples below:
 Rounded rectangle shape
 Three Point light rig type
 Circle bevel type
 Plastic material type
 Camera type defined by the orthographicFront preset
 Bevel width and height each equal to 190500
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
b (Bottom) [Example: Consider the following example of a light
direction from the bottom:
end example]
bl (Bottom Left) [Example: Consider the following example of a light
direction from the bottom left:
end example]
br (Bottom Right) [Example: Consider the following example of a light
direction from the bottom right:
2926 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2937 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
l (Left) [Example: Consider the following example of a light
direction from the left:
end example]
r (Right) [Example: Consider the following example of a light
direction from the right:
end example]
t (Top) [Example: Consider the following example of a light
©ISO/IEC 2016 – All rights reserved 2927\n\n--- Page 2938 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
direction from the top:
end example]
tl (Top Left) [Example: Consider the following example of a light
direction from the top left:
end example]
tr (Top Right) [Example: Consider the following example of a light
direction from the top right:
end example]
2928 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2939 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LightRigDirection) is located in
§A.4.1. end note]
20.1.10.30 ST_LightRigType (Light Rig Type)
Represents a preset light right that can be applied to a shape. The light rig represents a group of lights oriented
in a specific way relative to a 3D scene. The following properties were used to define the shape used in the
image examples below:
 Rounded rectangle shape
 Circle bevel type
 Warm Matte material type
 Camera type defined by the perspectiveContrastingRightFacing preset
 Bevel width and height each equal to 190500
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
balanced (Light Rig Enum ( Balanced )) Balanced
brightRoom (Bright Room) [Example: Consider the following example of the
brightRoom light rig applied to a basic shape:
end example]
chilly (Chilly) [Example: Consider the following example of the
chilly light rig applied to a basic shape:
©ISO/IEC 2016 – All rights reserved 2929\n\n--- Page 2940 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
contrasting (Contrasting) [Example: Consider the following example of the
contrasting light rig applied to a basic shape:
end example]
flat (Flat) [Example: Consider the following example of the flat
light rig applied to a basic shape:
end example]
flood (Flood) [Example: Consider the following example of the
flood light rig applied to a basic shape:
2930 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2941 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
freezing (Freezing) [Example: Consider the following example of the
freezing light rig applied to a basic shape:
end example]
glow (Glow) [Example: Consider the following example of the glow
light rig applied to a basic shape:
end example]
harsh (Harsh) [Example: Consider the following example of the
©ISO/IEC 2016 – All rights reserved 2931\n\n--- Page 2942 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
harsh light rig applied to a basic shape:
end example]
legacyFlat1 (Legacy Flat 1) [Example: Consider the following example of the
legacyFlat1 light rig applied to a basic shape:
end example]
legacyFlat2 (Legacy Flat 2) [Example: Consider the following example of the
legacyFlat2 light rig applied to a basic shape:
end example]
legacyFlat3 (Legacy Flat 3) [Example: Consider the following example of the
2932 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2943 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
legacyFlat3 light rig applied to a basic shape:
end example]
legacyFlat4 (Legacy Flat 4) [Example: Consider the following example of the
legacyFlat4 light rig applied to a basic shape:
end example]
legacyHarsh1 (Legacy Harsh 1) [Example: Consider the following example of the
legacyHarsh1 light rig applied to a basic shape:
end example]
©ISO/IEC 2016 – All rights reserved 2933\n\n--- Page 2944 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
legacyHarsh2 (Legacy Harsh 2) [Example: Consider the following example of the
legacyHarsh2 light rig applied to a basic shape:
end example]
legacyHarsh3 (Legacy Harsh 3) [Example: Consider the following example of the
legacyHarsh3 light rig applied to a basic shape:
end example]
legacyHarsh4 (Legacy Harsh 4) [Example: Consider the following example of the
legacyHarsh4 light rig applied to a basic shape:
end example]
2934 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2945 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
legacyNormal1 (Legacy Normal 1) [Example: Consider the following example of the
legacyNormal1 light rig applied to a basic shape:
end example]
legacyNormal2 (Legacy Normal 2) [Example: Consider the following example of the
legacyNormal2 light rig applied to a basic shape:
end example]
legacyNormal3 (Legacy Normal 3) [Example: Consider the following example of the
legacyNormal3 light rig applied to a basic shape:
end example]
©ISO/IEC 2016 – All rights reserved 2935\n\n--- Page 2946 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
legacyNormal4 (Legacy Normal 4) [Example: Consider the following example of the
legacyNormal4 light rig applied to a basic shape:
end example]
morning (Morning) [Example: Consider the following example of the
morning light rig applied to a basic shape:
end example]
soft (Soft) [Example: Consider the following example of the soft
light rig applied to a basic shape:
end example]
2936 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2947 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
sunrise (Sunrise) [Example: Consider the following example of the
sunrise light rig applied to a basic shape:
end example]
sunset (Sunset) [Example: Consider the following example of the
sunset light rig applied to a basic shape:
end example]
threePt (Three Point) [Example: Consider the following example of the
threePt light rig applied to a basic shape:
end example]
©ISO/IEC 2016 – All rights reserved 2937\n\n--- Page 2948 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
twoPt (Two Point) [Example: Consider the following example of the
twoPt light rig applied to a basic shape:
end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LightRigType) is located in
§A.4.1. end note]
20.1.10.31 ST_LineCap (End Line Cap)
This simple type specifies how to cap the ends of lines. This also affects the ends of line segments for dashed
lines.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
flat (Flat Line Cap) Line ends at end point.
rnd (Round Line Cap) Rounded ends. Semi-circle protrudes by half line
width.
sq (Square Line Cap) Square protrudes by half line width.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LineCap) is located in §A.4.1.
end note]
20.1.10.32 ST_LineEndLength (Line End Length)
This simple type represents the length of the line end decoration (e.g., arrowhead) relative to the width of the
line itself.
[Example: See the example images below. These samples have an arrow line end type and medium line end
width. end example]
2938 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2949 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
lg (Large)
Large
med (Medium)
Medium
sm (Small)
Small
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LineEndLength) is located in
§A.4.1. end note]
20.1.10.33 ST_LineEndType (Line End Type)
This simple type represents the shape decoration that appears at the ends of lines. For example, one choice is an
arrow head.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
arrow (Arrow Head) Line arrow head
diamond (Diamond) Diamond
none (None) No end
oval (Oval) Oval
stealth (Stealth Arrow) Stealth arrow head
triangle (Triangle Arrow Head) Triangle arrow head
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LineEndType) is located in
§A.4.1. end note]
20.1.10.34 ST_LineEndWidth (Line End Width)
This simple type represents the width of the line end decoration (e.g., arrowhead) relative to the width of the
line itself.
[Example: See the example images below. These samples have an arrow line end type and medium line end
length. end example]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 2939\n\n--- Page 2950 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
lg (Large)
Large
med (Medium)
Medium
sm (Small)
Small
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LineEndWidth) is located in
§A.4.1. end note]
20.1.10.35 ST_LineWidth (Line Width)
This simple type specifies the width of a line in EMUs. 1 pt = 12700 EMUs.
This simple type's contents are a restriction of the ST_Coordinate32Unqualified datatype (§20.1.10.18).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 20116800.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_LineWidth) is located in §A.4.1.
end note]
20.1.10.36 ST_OnOffStyleType (On/Off Style Type)
This simple type represents whether a style property should be applied.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
def (Default) Follow parent settings. For a themed property, follow
the theme settings. For an unthemed property, follow
the parent setting in the property inheritance chain.
off (Off) Property is off.
on (On) Property is on.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_OnOffStyleType) is located in
§A.4.1. end note]
2940 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2951 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.37 ST_PathFillMode (Path Fill Mode)
This simple type specifies the manner in which a path should be filled. The lightening and darkening of a path
allow for certain parts of the shape to be colored lighter of darker depending on user preference.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
darken (Darken Path Fill) This specifies that the corresponding path should have
a darker shaded color applied to it’s fill.
darkenLess (Darken Path Fill Less) This specifies that the corresponding path should have
a slightly darker shaded color applied to it’s fill.
lighten (Lighten Path Fill) This specifies that the corresponding path should have
a lightly shaded color applied to it’s fill.
lightenLess (Lighten Path Fill Less) This specifies that the corresponding path should have
a slightly lighter shaded color applied to it’s fill.
none (No Path Fill) This specifies that the corresponding path should have
no fill.
norm (Normal Path Fill) This specifies that the corresponding path should have
a normally shaded color applied to it’s fill.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PathFillMode) is located in
§A.4.1. end note]
20.1.10.38 ST_PathShadeType (Path Shade Type)
This simple type describes the shape of path to follow for a path gradient shade.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
circle (Circle) Gradient follows a circular path
rect (Rectangle) Gradient follows a rectangular path
shape (Shape) Gradient follows the shape
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PathShadeType) is located in
§A.4.1. end note]
20.1.10.39 ST_PenAlignment (Alignment Type)
This simple type specifies the Pen Alignment type for use within a text body.
©ISO/IEC 2016 – All rights reserved 2941\n\n--- Page 2952 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
ctr (Center Alignment) Center pen (line drawn at center of path stroke).
in (Inset Alignment) Inset pen (the pen is aligned on the inside of the edge
of the path).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PenAlignment) is located in
§A.4.1. end note]
20.1.10.40 ST_Percentage (Percentage)
This simple type specifies that its contents will contain a percentage value. See the union's member types for
details.
This simple type is a union of the following types:
 The ST_Percentage simple type (§22.9.2.9).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Percentage) is located in §A.4.1.
end note]
20.1.10.41 ST_PitchFamily (Pitch Family)
This simple type specifies a font pitch.
[Note: Although the type name is ST_PitchFamily, the integer value of this attribute specifies the font family
with the higher 4 bits and the font pitch with the lower 4 bits. end note]
This simple type's contents are a restriction of the W3C XML Schema byte datatype.
This simple type is restricted to the values listed in the following table:
Value Description
0x00 DEFAULT PITCH + UNKNOWN FONT FAMILY
0x01 FIXED PITCH + UNKNOWN FONT FAMILY
0x02 VARIABLE PITCH + UNKNOWN FONT FAMILY
0x10 DEFAULT PITCH + ROMAN FONT FAMILY
0x11 FIXED PITCH + ROMAN FONT FAMILY
0x12 VARIABLE PITCH + ROMAN FONT FAMILY
0x20 DEFAULT PITCH + SWISS FONT FAMILY
0x21 FIXED PITCH + SWISS FONT FAMILY
0x22 VARIABLE PITCH + SWISS FONT FAMILY
2942 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2953 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Value Description
0x30 DEFAULT PITCH + MODERN FONT FAMILY
0x31 FIXED PITCH + MODERN FONT FAMILY
0x32 VARIABLE PITCH + MODERN FONT FAMILY
0x40 DEFAULT PITCH + SCRIPT FONT FAMILY
0x41 FIXED PITCH + SCRIPT FONT FAMILY
0x42 VARIABLE PITCH + SCRIPT FONT FAMILY
0x50 DEFAULT PITCH + DECORATIVE FONT FAMILY
0x51 FIXED PITCH + DECORATIVE FONT FAMILY
0x52 VARIABLE PITCH + DECORATIVE FONT FAMILY
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PitchFamily) is located in §A.3.
end note]
20.1.10.42 ST_PositiveCoordinate (Positive Coordinate)
This simple type represents a positive position or length in EMUs.
This simple type's contents are a restriction of the W3C XML Schema long datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 27273042316900.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositiveCoordinate) is located in
§A.4.1. end note]
20.1.10.43 ST_PositiveCoordinate32 (Positive Coordinate Point)
This simple type specifies the a positive coordinate point that has a maximum size of 32 bits.
The units of measurement used here are EMUs (English Metric Units).
This simple type's contents are a restriction of the ST_Coordinate32Unqualified datatype (§20.1.10.18).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositiveCoordinate32) is located
in §A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 2943\n\n--- Page 2954 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.44 ST_PositiveFixedAngle (Positive Fixed Angle)
This simple type represents a positive angle in 60000ths of a degree. Range from [0, 360 degrees).
This simple type's contents are a restriction of the ST_Angle datatype (§20.1.10.3).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than 21600000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositiveFixedAngle) is located in
§A.4.1. end note]
20.1.10.45 ST_PositiveFixedPercentage (Positive Fixed Percentage)
This simple type specifies that its contents will contain a positive percentage value from zero through one
hundred percent. See the union's member types for details.
This simple type is a union of the following types:
 The ST_PositiveFixedPercentage simple type (§22.9.2.10).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositiveFixedPercentage) is
located in §A.4.1. end note]
20.1.10.46 ST_PositivePercentage (Positive Percentage Value with Sign)
This simple type specifies that its contents will contain a positive percentage value. See the union's member
types for details.
This simple type is a union of the following types:
 The ST_PositivePercentage simple type (§22.9.2.11).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositivePercentage) is located in
§A.4.1. end note]
20.1.10.47 ST_PresetCameraType (Preset Camera Type)
These enumeration values represent different algorithmic methods for setting all camera properties, including
position. The following example images below are all based off the following shape:
2944 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2955 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
In this image, we can see the shape has a camera pointing directly at the front face.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
isometricBottomDown (Isometric Bottom Down) [Example: Consider the following example of the
camera preset type:
end example]
isometricBottomUp (Isometric Bottom Up) [Example: Consider the following example of the
camera preset type:
end example]
isometricLeftDown (Isometric Left Down) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2945\n\n--- Page 2956 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
isometricLeftUp (Isometric Left Up) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis1Left (Isometric Off Axis 1 Left) [Example: Consider the following example of the
camera preset type:
end example]
2946 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2957 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
isometricOffAxis1Right (Isometric Off Axis 1 Right) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis1Top (Isometric Off Axis 1 Top) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis2Left (Isometric Off Axis 2 Left) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis2Right (Isometric Off Axis 2 Right) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2947\n\n--- Page 2958 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
isometricOffAxis2Top (Isometric Off Axis 2 Top) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis3Bottom (Isometric Off Axis 3 [Example: Consider the following example of the
Bottom) camera preset type:
end example]
isometricOffAxis3Left (Isometric Off Axis 3 Left) [Example: Consider the following example of the
camera preset type:
2948 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2959 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
isometricOffAxis3Right (Isometric Off Axis 3 Right) [Example: Consider the following example of the
camera preset type:
end example]
isometricOffAxis4Bottom (Isometric Off Axis 4 [Example: Consider the following example of the
Bottom) camera preset type:
end example]
isometricOffAxis4Left (Isometric Off Axis 4 Left) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2949\n\n--- Page 2960 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
isometricOffAxis4Right (Isometric Off Axis 4 Right) [Example: Consider the following example of the
camera preset type:
end example]
isometricRightDown (Isometric Right Down) [Example: Consider the following example of the
camera preset type:
end example]
2950 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2961 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
isometricRightUp (Isometric Right Up) [Example: Consider the following example of the
camera preset type:
end example]
isometricTopDown (Isometric Top Down) [Example: Consider the following example of the
camera preset type:
end example]
isometricTopUp (Isometric Top Up) [Example: Consider the following example of the
camera preset type:
end example]
legacyObliqueBottom (Legacy Oblique Bottom) [Example: Consider the following example of the
©ISO/IEC 2016 – All rights reserved 2951\n\n--- Page 2962 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
camera preset type:
end example]
legacyObliqueBottomLeft (Legacy Oblique Bottom [Example: Consider the following example of the
Left) camera preset type:
end example]
legacyObliqueBottomRight (Legacy Oblique Bottom [Example: Consider the following example of the
Right) camera preset type:
end example]
legacyObliqueFront (Legacy Oblique Front) [Example: Consider the following example of the
camera preset type:
2952 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2963 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
legacyObliqueLeft (Legacy Oblique Left) [Example: Consider the following example of the
camera preset type:
end example]
legacyObliqueRight (Legacy Oblique Right) [Example: Consider the following example of the
camera preset type:
end example]
legacyObliqueTop (Legacy Oblique Top) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2953\n\n--- Page 2964 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
legacyObliqueTopLeft (Legacy Oblique Top Left) [Example: Consider the following example of the
camera preset type:
end example]
legacyObliqueTopRight (Legacy Oblique Top Right) [Example: Consider the following example of the
camera preset type:
end example]
legacyPerspectiveBottom (Legacy Perspective [Example: Consider the following example of the
Bottom) camera preset type:
2954 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2965 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
legacyPerspectiveBottomLeft (Legacy Perspective [Example: Consider the following example of the
Bottom Left) camera preset type:
end example]
legacyPerspectiveBottomRight (Legacy Perspective [Example: Consider the following example of the
Bottom Right) camera preset type:
end example]
legacyPerspectiveFront (Legacy Perspective Front) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2955\n\n--- Page 2966 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
legacyPerspectiveLeft (Legacy Perspective Left) [Example: Consider the following example of the
camera preset type:
end example]
legacyPerspectiveRight (Legacy Perspective Right) [Example: Consider the following example of the
camera preset type:
end example]
legacyPerspectiveTop (Legacy Perspective Top) [Example: Consider the following example of the
camera preset type:
2956 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2967 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
legacyPerspectiveTopLeft (Legacy Perspective Top [Example: Consider the following example of the
Left) camera preset type:
end example]
legacyPerspectiveTopRight (Legacy Perspective Top [Example: Consider the following example of the
Right) camera preset type:
end example]
obliqueBottom (Oblique Bottom) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2957\n\n--- Page 2968 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
obliqueBottomLeft (Oblique Bottom Left) [Example: Consider the following example of the
camera preset type:
end example]
obliqueBottomRight (Oblique Bottom Right) [Example: Consider the following example of the
camera preset type:
end example]
obliqueLeft (Oblique Left) [Example: Consider the following example of the
camera preset type:
2958 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2969 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
obliqueRight (Oblique Right) [Example: Consider the following example of the
camera preset type:
end example]
obliqueTop (Oblique Top) [Example: Consider the following example of the
camera preset type:
end example]
obliqueTopLeft (Oblique Top Left) [Example: Consider the following example of the
camera preset type:
©ISO/IEC 2016 – All rights reserved 2959\n\n--- Page 2970 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
obliqueTopRight (Oblique Top Right) [Example: Consider the following example of the
camera preset type:
end example]
orthographicFront (Orthographic Front) [Example: Consider the following example of the
camera preset type:
end example]
perspectiveAbove (Orthographic Above) [Example: Consider the following example of the
camera preset type:
2960 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2971 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
perspectiveAboveLeftFacing (Perspective Above Left [Example: Consider the following example of the
Facing) camera preset type:
end example]
perspectiveAboveRightFacing (Perspective Above [Example: Consider the following example of the
Right Facing) camera preset type:
end example]
perspectiveBelow (Perspective Below) [Example: Consider the following example of the
©ISO/IEC 2016 – All rights reserved 2961\n\n--- Page 2972 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
camera preset type:
end example]
perspectiveContrastingLeftFacing (Perspective [Example: Consider the following example of the
Contrasting Left Facing) camera preset type:
end example]
perspectiveContrastingRightFacing (Perspective [Example: Consider the following example of the
Contrasting Right Facing) camera preset type:
end example]
perspectiveFront (Perspective Front) [Example: Consider the following example of the
2962 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2973 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
camera preset type:
end example]
perspectiveHeroicExtremeLeftFacing (Perspective [Example: Consider the following example of the
Heroic Extreme Left Facing) camera preset type:
end example]
perspectiveHeroicExtremeRightFacing (Perspective [Example: Consider the following example of the
Heroic Extreme Right Facing) camera preset type:
end example]
perspectiveHeroicLeftFacing (Perspective Heroic Left [Example: Consider the following example of the
Facing) camera preset type:
©ISO/IEC 2016 – All rights reserved 2963\n\n--- Page 2974 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
perspectiveHeroicRightFacing (Perspective Heroic [Example: Consider the following example of the
Right Facing) camera preset type:
end example]
perspectiveLeft (Perspective Left) [Example: Consider the following example of the
camera preset type:
end example]
perspectiveRelaxed (Perspective Relaxed) [Example: Consider the following example of the
camera preset type:
2964 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2975 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
perspectiveRelaxedModerately (Perspective Relaxed [Example: Consider the following example of the
Moderately) camera preset type:
end example]
perspectiveRight (Perspective Right) [Example: Consider the following example of the
camera preset type:
end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetCameraType) is located in
§A.4.1. end note]
20.1.10.48 ST_PresetColorVal (Preset Color Value)
This simple type represents a preset color value.
©ISO/IEC 2016 – All rights reserved 2965\n\n--- Page 2976 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
aliceBlue (Alice Blue Preset Color) Specifies a color with RGB value (240,248,255)
antiqueWhite (Antique White Preset Color) Specifies a color with RGB value (250,235,215)
aqua (Aqua Preset Color) Specifies a color with RGB value (0,255,255)
aquamarine (Aquamarine Preset Color) Specifies a color with RGB value (127,255,212)
azure (Azure Preset Color) Specifies a color with RGB value (240,255,255)
beige (Beige Preset Color) Specifies a color with RGB value (245,245,220)
bisque (Bisque Preset Color) Specifies a color with RGB value (255,228,196)
black (Black Preset Color) Specifies a color with RGB value (0,0,0)
blanchedAlmond (Blanched Almond Preset Color) Specifies a color with RGB value (255,235,205)
blue (Blue Preset Color) Specifies a color with RGB value (0,0,255)
blueViolet (Blue Violet Preset Color) Specifies a color with RGB value (138,43,226)
brown (Brown Preset Color) Specifies a color with RGB value (165,42,42)
burlyWood (Burly Wood Preset Color) Specifies a color with RGB value (222,184,135)
cadetBlue (Cadet Blue Preset Color) Specifies a color with RGB value (95,158,160)
chartreuse (Chartreuse Preset Color) Specifies a color with RGB value (127,255,0)
chocolate (Chocolate Preset Color) Specifies a color with RGB value (210,105,30)
coral (Coral Preset Color) Specifies a color with RGB value (255,127,80)
cornflowerBlue (Cornflower Blue Preset Color) Specifies a color with RGB value (100,149,237)
cornsilk (Cornsilk Preset Color) Specifies a color with RGB value (255,248,220)
crimson (Crimson Preset Color) Specifies a color with RGB value (220,20,60)
cyan (Cyan Preset Color) Specifies a color with RGB value (0,255,255)
darkBlue (Dark Blue Preset Color) Specifies a color with RGB value (0,0,139)
darkCyan (Dark Cyan Preset Color) Specifies a color with RGB value (0,139,139)
darkGoldenrod (Dark Goldenrod Preset Color) Specifies a color with RGB value (184,134,11)
darkGray (Dark Gray Preset Color) Specifies a color with RGB value (169,169,169)
darkGreen (Dark Green Preset Color) Specifies a color with RGB value (0,100,0)
darkGrey (Dark Gray Preset Color) Specifies a color with RGB value (169,169,169)
darkKhaki (Dark Khaki Preset Color) Specifies a color with RGB value (189,183,107)
darkMagenta (Dark Magenta Preset Color) Specifies a color with RGB value (139,0,139)
darkOliveGreen (Dark Olive Green Preset Color) Specifies a color with RGB value (85,107,47)
darkOrange (Dark Orange Preset Color) Specifies a color with RGB value (255,140,0)
darkOrchid (Dark Orchid Preset Color) Specifies a color with RGB value (153,50,204)
2966 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2977 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
darkRed (Dark Red Preset Color) Specifies a color with RGB value (139,0,0)
darkSalmon (Dark Salmon Preset Color) Specifies a color with RGB value (233,150,122)
darkSeaGreen (Dark Sea Green Preset Color) Specifies a color with RGB value (143,188,143)
darkSlateBlue (Dark Slate Blue Preset Color) Specifies a color with RGB value (72,61,139)
darkSlateGray (Dark Slate Gray Preset Color) Specifies a color with RGB value (47,79,79)
darkSlateGrey (Dark Slate Gray Preset Color) Specifies a color with RGB value (47,79,79)
darkTurquoise (Dark Turquoise Preset Color) Specifies a color with RGB value (0,206,209)
darkViolet (Dark Violet Preset Color) Specifies a color with RGB value (148,0,211)
deepPink (Deep Pink Preset Color) Specifies a color with RGB value (255,20,147)
deepSkyBlue (Deep Sky Blue Preset Color) Specifies a color with RGB value (0,191,255)
dimGray (Dim Gray Preset Color) Specifies a color with RGB value (105,105,105)
dimGrey (Dim Gray Preset Color) Specifies a color with RGB value (105,105,105)
dkBlue (Dark Blue Preset Color) Specifies a color with RGB value (0,0,139)
dkCyan (Dark Cyan Preset Color) Specifies a color with RGB value (0,139,139)
dkGoldenrod (Dark Goldenrod Preset Color) Specifies a color with RGB value (184,134,11)
dkGray (Dark Gray Preset Color) Specifies a color with RGB value (169,169,169)
dkGreen (Dark Green Preset Color) Specifies a color with RGB value (0,100,0)
dkGrey (Dark Gray Preset Color) Specifies a color with RGB value (169,169,169)
dkKhaki (Dark Khaki Preset Color) Specifies a color with RGB value (189,183,107)
dkMagenta (Dark Magenta Preset Color) Specifies a color with RGB value (139,0,139)
dkOliveGreen (Dark Olive Green Preset Color) Specifies a color with RGB value (85,107,47)
dkOrange (Dark Orange Preset Color) Specifies a color with RGB value (255,140,0)
dkOrchid (Dark Orchid Preset Color) Specifies a color with RGB value (153,50,204)
dkRed (Dark Red Preset Color) Specifies a color with RGB value (139,0,0)
dkSalmon (Dark Salmon Preset Color) Specifies a color with RGB value (233,150,122)
dkSeaGreen (Dark Sea Green Preset Color) Specifies a color with RGB value (143,188,139)
dkSlateBlue (Dark Slate Blue Preset Color) Specifies a color with RGB value (72,61,139)
dkSlateGray (Dark Slate Gray Preset Color) Specifies a color with RGB value (47,79,79)
dkSlateGrey (Dark Slate Gray Preset Color) Specifies a color with RGB value (47,79,79)
dkTurquoise (Dark Turquoise Preset Color) Specifies a color with RGB value (0,206,209)
dkViolet (Dark Violet Preset Color) Specifies a color with RGB value (148,0,211)
dodgerBlue (Dodger Blue Preset Color) Specifies a color with RGB value (30,144,255)
firebrick (Firebrick Preset Color) Specifies a color with RGB value (178,34,34)
floralWhite (Floral White Preset Color) Specifies a color with RGB value (255,250,240)
©ISO/IEC 2016 – All rights reserved 2967\n\n--- Page 2978 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
forestGreen (Forest Green Preset Color) Specifies a color with RGB value (34,139,34)
fuchsia (Fuchsia Preset Color) Specifies a color with RGB value (255,0,255)
gainsboro (Gainsboro Preset Color) Specifies a color with RGB value (220,220,220)
ghostWhite (Ghost White Preset Color) Specifies a color with RGB value (248,248,255)
gold (Gold Preset Color) Specifies a color with RGB value (255,215,0)
goldenrod (Goldenrod Preset Color) Specifies a color with RGB value (218,165,32)
gray (Gray Preset Color) Specifies a color with RGB value (128,128,128)
green (Green Preset Color) Specifies a color with RGB value (0,128,0)
greenYellow (Green Yellow Preset Color) Specifies a color with RGB value (173,255,47)
grey (Gray Preset Color) Specifies a color with RGB value (128,128,128)
honeydew (Honeydew Preset Color) Specifies a color with RGB value (240,255,240)
hotPink (Hot Pink Preset Color) Specifies a color with RGB value (255,105,180)
indianRed (Indian Red Preset Color) Specifies a color with RGB value (205,92,92)
indigo (Indigo Preset Color) Specifies a color with RGB value (75,0,130)
ivory (Ivory Preset Color) Specifies a color with RGB value (255,255,240)
khaki (Khaki Preset Color) Specifies a color with RGB value (240,230,140)
lavender (Lavender Preset Color) Specifies a color with RGB value (230,230,250)
lavenderBlush (Lavender Blush Preset Color) Specifies a color with RGB value (255,240,245)
lawnGreen (Lawn Green Preset Color) Specifies a color with RGB value (124,252,0)
lemonChiffon (Lemon Chiffon Preset Color) Specifies a color with RGB value (255,250,205)
lightBlue (Light Blue Preset Color) Specifies a color with RGB value (173,216,230)
lightCoral (Light Coral Preset Color) Specifies a color with RGB value (240,128,128)
lightCyan (Light Cyan Preset Color) Specifies a color with RGB value (224,255,255)
lightGoldenrodYellow (Light Goldenrod Yellow Preset Specifies a color with RGB value (250,250,210)
Color)
lightGray (Light Gray Preset Color) Specifies a color with RGB value (211,211,211)
lightGreen (Light Green Preset Color) Specifies a color with RGB value (144,238,144)
lightGrey (Light Gray Preset Color) Specifies a color with RGB value (211,211,211)
lightPink (Light Pink Preset Color) Specifies a color with RGB value (255,182,193)
lightSalmon (Light Salmon Preset Color) Specifies a color with RGB value (255,160,122)
lightSeaGreen (Light Sea Green Preset Color) Specifies a color with RGB value (32,178,170)
lightSkyBlue (Light Sky Blue Preset Color) Specifies a color with RGB value (135,206,250)
lightSlateGray (Light Slate Gray Preset Color) Specifies a color with RGB value (119,136,153)
lightSlateGrey (Light Slate Gray Preset Color) Specifies a color with RGB value (119,136,153)
2968 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2979 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
lightSteelBlue (Light Steel Blue Preset Color) Specifies a color with RGB value (176,196,222)
lightYellow (Light Yellow Preset Color) Specifies a color with RGB value (255,255,224)
lime (Lime Preset Color) Specifies a color with RGB value (0,255,0)
limeGreen (Lime Green Preset Color) Specifies a color with RGB value (50,205,50)
linen (Linen Preset Color) Specifies a color with RGB value (250,240,230)
ltBlue (Light Blue Preset Color) Specifies a color with RGB value (173,216,230)
ltCoral (Light Coral Preset Color) Specifies a color with RGB value (240,128,128)
ltCyan (Light Cyan Preset Color) Specifies a color with RGB value (224,255,255)
ltGoldenrodYellow (Light Goldenrod Yellow Preset Specifies a color with RGB value (250,250,120)
Color)
ltGray (Light Gray Preset Color) Specifies a color with RGB value (211,211,211)
ltGreen (Light Green Preset Color) Specifies a color with RGB value (144,238,144)
ltGrey (Light Gray Preset Color) Specifies a color with RGB value (211,211,211)
ltPink (Light Pink Preset Color) Specifies a color with RGB value (255,182,193)
ltSalmon (Light Salmon Preset Color) Specifies a color with RGB value (255,160,122)
ltSeaGreen (Light Sea Green Preset Color) Specifies a color with RGB value (32,178,170)
ltSkyBlue (Light Sky Blue Preset Color) Specifies a color with RGB value (135,206,250)
ltSlateGray (Light Slate Gray Preset Color) Specifies a color with RGB value (119,136,153)
ltSlateGrey (Light Slate Gray Preset Color) Specifies a color with RGB value (119,136,153)
ltSteelBlue (Light Steel Blue Preset Color) Specifies a color with RGB value (176,196,222)
ltYellow (Light Yellow Preset Color) Specifies a color with RGB value (255,255,224)
magenta (Magenta Preset Color) Specifies a color with RGB value (255,0,255)
maroon (Maroon Preset Color) Specifies a color with RGB value (128,0,0)
medAquamarine (Medium Aquamarine Preset Color) Specifies a color with RGB value (102,205,170)
medBlue (Medium Blue Preset Color) Specifies a color with RGB value (0,0,205)
mediumAquamarine (Medium Aquamarine Preset Specifies a color with RGB value (102,205,170)
Color)
mediumBlue (Medium Blue Preset Color) Specifies a color with RGB value (0,0,205)
mediumOrchid (Medium Orchid Preset Color) Specifies a color with RGB value (186,85,211)
mediumPurple (Medium Purple Preset Color) Specifies a color with RGB value (147,112,219)
mediumSeaGreen (Medium Sea Green Preset Color) Specifies a color with RGB value (60,179,113)
mediumSlateBlue (Medium Slate Blue Preset Color) Specifies a color with RGB value (123,104,238)
mediumSpringGreen (Medium Spring Green Preset Specifies a color with RGB value (0,250,154)
Color)
mediumTurquoise (Medium Turquoise Preset Color) Specifies a color with RGB value (72,209,204)
©ISO/IEC 2016 – All rights reserved 2969\n\n--- Page 2980 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
mediumVioletRed (Medium Violet Red Preset Color) Specifies a color with RGB value (199,21,133)
medOrchid (Medium Orchid Preset Color) Specifies a color with RGB value (186,85,211)
medPurple (Medium Purple Preset Color) Specifies a color with RGB value (147,112,219)
medSeaGreen (Medium Sea Green Preset Color) Specifies a color with RGB value (60,179,113)
medSlateBlue (Medium Slate Blue Preset Color) Specifies a color with RGB value (123,104,238)
medSpringGreen (Medium Spring Green Preset Color) Specifies a color with RGB value (0,250,154)
medTurquoise (Medium Turquoise Preset Color) Specifies a color with RGB value (72,209,204)
medVioletRed (Medium Violet Red Preset Color) Specifies a color with RGB value (199,21,133)
midnightBlue (Midnight Blue Preset Color) Specifies a color with RGB value (25,25,112)
mintCream (Mint Cream Preset Color) Specifies a color with RGB value (245,255,250)
mistyRose (Misty Rose Preset Color) Specifies a color with RGB value (255,228,225)
moccasin (Moccasin Preset Color) Specifies a color with RGB value (255,228,181)
navajoWhite (Navajo White Preset Color) Specifies a color with RGB value (255,222,173)
navy (Navy Preset Color) Specifies a color with RGB value (0,0,128)
oldLace (Old Lace Preset Color) Specifies a color with RGB value (253,245,230)
olive (Olive Preset Color) Specifies a color with RGB value (128,128,0)
oliveDrab (Olive Drab Preset Color) Specifies a color with RGB value (107,142,35)
orange (Orange Preset Color) Specifies a color with RGB value (255,165,0)
orangeRed (Orange Red Preset Color) Specifies a color with RGB value (255,69,0)
orchid (Orchid Preset Color) Specifies a color with RGB value (218,112,214)
paleGoldenrod (Pale Goldenrod Preset Color) Specifies a color with RGB value (238,232,170)
paleGreen (Pale Green Preset Color) Specifies a color with RGB value (152,251,152)
paleTurquoise (Pale Turquoise Preset Color) Specifies a color with RGB value (175,238,238)
paleVioletRed (Pale Violet Red Preset Color) Specifies a color with RGB value (219,112,147)
papayaWhip (Papaya Whip Preset Color) Specifies a color with RGB value (255,239,213)
peachPuff (Peach Puff Preset Color) Specifies a color with RGB value (255,218,185)
peru (Peru Preset Color) Specifies a color with RGB value (205,133,63)
pink (Pink Preset Color) Specifies a color with RGB value (255,192,203)
plum (Plum Preset Color) Specifies a color with RGB value (221,160,221)
powderBlue (Powder Blue Preset Color) Specifies a color with RGB value (176,224,230)
purple (Purple Preset Color) Specifies a color with RGB value (128,0,128)
red (Red Preset Color) Specifies a color with RGB value (255,0,0)
rosyBrown (Rosy Brown Preset Color) Specifies a color with RGB value (188,143,143)
royalBlue (Royal Blue Preset Color) Specifies a color with RGB value (65,105,225)
2970 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2981 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
saddleBrown (Saddle Brown Preset Color) Specifies a color with RGB value (139,69,19)
salmon (Salmon Preset Color) Specifies a color with RGB value (250,128,114)
sandyBrown (Sandy Brown Preset Color) Specifies a color with RGB value (244,164,96)
seaGreen (Sea Green Preset Color) Specifies a color with RGB value (46,139,87)
seaShell (Sea Shell Preset Color) Specifies a color with RGB value (255,245,238)
sienna (Sienna Preset Color) Specifies a color with RGB value (160,82,45)
silver (Silver Preset Color) Specifies a color with RGB value (192,192,192)
skyBlue (Sky Blue Preset Color) Specifies a color with RGB value (135,206,235)
slateBlue (Slate Blue Preset Color) Specifies a color with RGB value (106,90,205)
slateGray (Slate Gray Preset Color) Specifies a color with RGB value (112,128,144)
slateGrey (Slate Gray Preset Color) Specifies a color with RGB value (112,128,144)
snow (Snow Preset Color) Specifies a color with RGB value (255,250,250)
springGreen (Spring Green Preset Color) Specifies a color with RGB value (0,255,127)
steelBlue (Steel Blue Preset Color) Specifies a color with RGB value (70,130,180)
tan (Tan Preset Color) Specifies a color with RGB value (210,180,140)
teal (Teal Preset Color) Specifies a color with RGB value (0,128,128)
thistle (Thistle Preset Color) Specifies a color with RGB value (216,191,216)
tomato (Tomato Preset Color) Specifies a color with RGB value (255,99,71)
turquoise (Turquoise Preset Color) Specifies a color with RGB value (64,224,208)
violet (Violet Preset Color) Specifies a color with RGB value (238,130,238)
wheat (Wheat Preset Color) Specifies a color with RGB value (245,222,179)
white (White Preset Color) Specifies a color with RGB value (255,255,255)
whiteSmoke (White Smoke Preset Color) Specifies a color with RGB value (245,245,245)
yellow (Yellow Preset Color) Specifies a color with RGB value (255,255,0)
yellowGreen (Yellow Green Preset Color) Specifies a color with RGB value (154,205,50)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetColorVal) is located in
§A.4.1. end note]
20.1.10.49 ST_PresetLineDashVal (Preset Line Dash Value)
This simple type represents preset line dash values. The description for each style shows an illustration of the
line style. Each style also contains a precise binary representation of the repeating dash style. Each 1
corresponds to a line segment of the same length as the line width, and each 0 corresponds to a space of the
same length as the line width.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 2971\n\n--- Page 2982 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
dash (Dash)
1111000
dashDot (Dash Dot)
11110001000
dot (Dot)
1000
lgDash (Large Dash)
11111111000
lgDashDot (Large Dash Dot)
111111110001000
lgDashDotDot (Large Dash Dot Dot)
1111111100010001000
solid (Solid)
1
sysDash (System Dash)
1110
sysDashDot (System Dash Dot)
111010
sysDashDotDot (System Dash Dot Dot)
11101010
sysDot (System Dot)
10
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetLineDashVal) is located in
§A.4.1. end note]
20.1.10.50 ST_PresetMaterialType (Preset Material Type)
Describes surface appearance of a shape. The material type combines with lighting characteristics to create the
final look and feel of a shape. The set of material properties which can be combined together to create the
presets below consist of the following characteristics:
 Specular color – This defines the color of the highlight associated with the material.
 Specular power – This defines the size and how intense the highlight is. Smaller values provide a larger,
but less intense highlight, while larger values provide a smaller, but more intense highlight.
 Diffuse color – This defines the perceived color of the material where an object is directly illuminated by
a light source. Generally speaking, the default color here would be based on the shape fill color.
2972 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2983 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Ambient color – This defines the perceived color of the material where an object is not directly
illuminated by a light source. Generally speaking, the default color here would be based on the shape
fill color.
 Emissive color – This defines the color of a light which is perceived to be given off by an object.
 Diffuse Fresnel effect – This is an effect that either darkens (approaches black) or lightens (approaches
white) the diffuse color of the material type at glancing angles. Positive values cause the material to
become brighter, negative values cause the material to become darker.
 Alpha Fresnel effect – This is an effect that either makes the material more opaque or more transparent
at glancing angles. Positive values cause the material to become more opaque, negative values cause
the material to become more transparent.
In the following examples, the exact values given for certain properties should be understood to be relative
values in order to provide a reference. These values could be different depending upon technologies used to
render the material types. The following properties were used to define the shape used in the image examples
below:
 Rounded rectangle shape
 Circle bevel type
 Three Point light rig type
 Camera type defined by the perspectiveContrastingRightFacing preset
 Bevel width and height each equal to 190500
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
clear (Clear) The clear material type has the following
characteristics:
 Specular Color: light gray
 Diffuse Color: shape fill color with 90% alpha
 Ambient Color: shape fill color with 90% alpha
 Emissive Color: black
 Diffuse Fresnel value: -8
 Alpha Fresnel value: 1
[Example: Consider the following example of the
clear material type:
©ISO/IEC 2016 – All rights reserved 2973\n\n--- Page 2984 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
dkEdge (Dark Edge) The dkEdge material type has the following
characteristics:
 Specular Color: white
 Specular Power value: 35
 Ambient Color: shape fill color
 Emissive Color: black
 Diffuse Fresnel value: -2
[Example: Consider the following example of the
dkEdge material type:
end example]
flat (Flat) The flat material type has the following
characteristics:
 Specular Color: very light gray
 Specular Power value: 50
 Diffuse Color: black
 Ambient Color: black
 Emissive Color: shape fill color
 Diffuse Fresnel value: -4
2974 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2985 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Example: Consider the following example of the flat
material type:
end example]
legacyMatte (Legacy Matte) The legacyMatte material type has the following
characteristics:
 Specular Color: black
 Ambient Color: shape fill color
 Emissive Color: black
 Diffuse Fresnel value: -4
[Example: Consider the following example of the
legacyMatte material type:
end example]
legacyMetal (Legacy Metal) The legacyMetal material type has the following
characteristics:
 Specular Color: shape fill color
 Specular Power value: 32
 Diffuse Color: shape fill color darkened by
adding black
 Ambient Color: shape fill color darkened by
adding black
©ISO/IEC 2016 – All rights reserved 2975\n\n--- Page 2986 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
 Emissive Color: black
[Example: Consider the following example of the
legacyMetal material type:
end example]
legacyPlastic (Legacy Plastic) The legacyPlastic material type has the following
characteristics:
 Specular Color: white
 Specular Power value: 32
 Ambient Color: shape fill color
 Emissive Color: black
[Example: Consider the following example of the
legacyPlastic material type:
end example]
legacyWireframe (Legacy Wireframe) The legacyWireframe material type has none of the
associated material properties and is based on a
wireframe interpretation of the shape.
[Example: Consider the following example of the
legacyWireframe material type:
2976 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2987 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
matte (Matte) The matte material type has the following
characteristics:
 Specular Color: black
 Ambient Color: shape fill color
 Emissive Color: black
[Example: Consider the following example of the
matte material type:
end example]
metal (Metal) The metal material type has the following
characteristics:
 Specular Color: shape fill color plus white,
which is brightened by 1.5 times the normal
value
 Specular Power value: 12
 Ambient Color: shape fill color
 Emissive Color: black
 Diffuse Fresnel value: 4
[Example: Consider the following example of the
©ISO/IEC 2016 – All rights reserved 2977\n\n--- Page 2988 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
metal material type:
end example]
plastic (Plastic) The plastic material type has the following
characteristics:
 Specular Color: light gray
 Specular Power value: 12
 Ambient Color: shape fill color
 Emissive Color: black
[Example: Consider the following example of the
plastic material type:
end example]
powder (Powder) The powder material type has the following
characteristics:
 Specular Color: dark gray
 Specular Power value: 10
 Diffuse Color: gray
 Ambient Color: gray
 Emissive Color: black
 Diffuse Fresnel value: 2
2978 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2989 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Example: Consider the following example of the
powder material type:
end example]
softEdge (Soft Edge) The softEdge material type has the following
characteristics:
 Specular Color: white
 Specular Power value: 35
 Ambient Color: shape fill color
 Emissive Color: black
 Diffuse Fresnel value: 4
 Alpha Fresnel value: -10
[Example: Consider the following example of the
softEdge material type:
end example]
softmetal (Soft Metal) The softMetal material type has the following
characteristics:
 Specular Color: shape fill color lightened with
white by 50%
 Specular Power value: 8
©ISO/IEC 2016 – All rights reserved 2979\n\n--- Page 2990 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
 Ambient Color: shape fill color
 Emissive Color: black
[Example: Consider the following example of the
softmetal material type:
end example]
translucentPowder (Translucent Powder) The translucentPowder material type has the
following characteristics:
 Specular Color: dark gray
 Specular Power value: 10
 Diffuse Color: shape fill color with 30%
transparency
 Ambient Color: shape fill color with 30%
transparency
 Emissive Color: black
 Diffuse Fresnel value: 2
 Alpha Fresnel value: -1
[Example: Consider the following example of the
translucentPowder material type:
end example]
2980 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2991 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
warmMatte (Warm Matte) The warmMatte material type has the following
characteristics:
 Specular Color: dark gray
 Specular Power value: 8
 Ambient Color: shape fill color
 Emissive Color: black
[Example: Consider the following example of the
warmMatte material type:
end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetMaterialType) is located
in §A.4.1. end note]
20.1.10.51 ST_PresetPatternVal (Preset Pattern Value)
This simple type indicates a preset type of pattern fill. The description of each value contains an illustration of
the fill type.
[Note: These presets correspond to members of the HatchStyle enumeration in the Microsoft .NET Framework.
A reference for this type can be found at http://msdn2.microsoft.com/en-
us/library/system.drawing.drawing2d.hatchstyle.aspx. end note]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
cross (Cross)
dashDnDiag (Dashed Downward Diagonal)
©ISO/IEC 2016 – All rights reserved 2981\n\n--- Page 2992 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
dashHorz (Dashed Horizontal)
dashUpDiag (Dashed Upward DIagonal)
dashVert (Dashed Vertical)
diagBrick (Diagonal Brick)
diagCross (Diagonal Cross)
divot (Divot)
dkDnDiag (Dark Downward Diagonal)
dkHorz (Dark Horizontal)
dkUpDiag (Dark Upward Diagonal)
dkVert (Dark Vertical)
dnDiag (Downward Diagonal)
dotDmnd (Dotted Diamond)
dotGrid (Dotted Grid)
horz (Horizontal)
horzBrick (Horizontal Brick)
lgCheck (Large Checker Board)
lgConfetti (Large Confetti)
lgGrid (Large Grid)
ltDnDiag (Light Downward Diagonal)
ltHorz (Light Horizontal)
2982 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2993 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
ltUpDiag (Light Upward Diagonal)
ltVert (Light Vertical)
narHorz (Narrow Horizontal)
narVert (Narrow Vertical)
openDmnd (Open Diamond)
pct10 (10%)
pct20 (20%)
pct25 (25%)
pct30 (30%)
pct40 (40%)
pct5 (5%)
pct50 (50%)
pct60 (60%)
pct70 (70%)
pct75 (75%)
pct80 (80%)
pct90 (90%)
plaid (Plaid)
shingle (Shingle)
smCheck (Small Checker Board)
©ISO/IEC 2016 – All rights reserved 2983\n\n--- Page 2994 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
smConfetti (Small Confetti)
smGrid (Small Grid)
solidDmnd (Solid Diamond)
sphere (Sphere)
trellis (Trellis)
upDiag (Upward Diagonal)
vert (Vertical)
wave (Wave)
wdDnDiag (Wide Downward Diagonal)
wdUpDiag (Wide Upward Diagonal)
weave (Weave)
zigZag (Zig Zag)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetPatternVal) is located in
§A.4.1. end note]
20.1.10.52 ST_PresetShadowVal (Preset Shadow Type)
This simple type indicates one of 20 preset shadow types. Each enumeration value description illustrates the
type of shadow represented by the value. Each description contains the parameters to the outer shadow effect
represented by the preset, in addition to those attributes common to all prstShdw effects.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
shdw1 (Top Left Drop Shadow)
No additional attributes specified.
2984 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2995 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
shdw10 (Top Left Large Drop Shadow)
align = "br"
sx = 125%
sy = 125%
shdw11 (Back Left Long Perspective Shadow)
align = "b"
kx = 40.89°
sy = 50%
shdw12 (Back Right Long Perspective Shadow)
align = "b"
kx = -40.89°
sy = 50%
shdw13 (Top Left Double Drop Shadow)
Equivalent to two outer shadow effects.
Shadow 1:
No additional attributes specified.
Shadow 2:
color = min(1, shadow 1's color (0 <= r, g, b <= 1) +
102/255), per r, g, b component
dist = 2 * shadow 1's distance
shdw14 (Bottom Right Small Drop Shadow)
No additional attributes specified.
shdw15 (Front Left Long Perspective Shadow)
align = "b"
kx = 40.89°
sy = -50%
shdw16 (Front Right LongPerspective Shadow)
align = "b"
kx = -40.89°
sy = -50%
shdw17 (3D Outer Box Shadow)
Equivalent to two outer shadow effects.
Shadow 1:
No additional attributes specified.
©ISO/IEC 2016 – All rights reserved 2985\n\n--- Page 2996 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
Shadow 2:
color = min(1, shadow 1's color (0 <= r, g, b <= 1) +
102/255), per r, g, b component
dir = shadow 1's direction + 180°
shdw18 (3D Inner Box Shadow)
Equivalent to two outer shadow effects.
Shadow 1:
No additional attributes specified.
Shadow 2:
color = min(1, shadow 1's color (0 <= r, g, b <= 1) +
102/255), per r, g, b component
dir = shadow 1's direction + 180°
shdw19 (Back Center Perspective Shadow)
align = "b"
sy = 50°
shdw2 (Top Right Drop Shadow)
No additional attributes specified.
shdw20 (Front Bottom Shadow)
align = "b"
sy = -100°
shdw3 (Back Left Perspective Shadow)
align = "b"
ky = 40.89°
sy = 50%
shdw4 (Back Right Perspective Shadow)
align = "b"
kx = -40.89°
sy = 50%
shdw5 (Bottom Left Drop Shadow)
No additional attributes specified.
shdw6 (Bottom Right Drop Shadow)
No additional attributes specified.
shdw7 (Front Left Perspective Shadow)
2986 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2997 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
align = "b"
kx = 40.89°
sy = -50%
shdw8 (Front Right Perspective Shadow)
align = "b"
kx = -40.89°
sy = -50%
shdw9 (Top Left Small Drop Shadow)
align = "tl"
sx = 75%
sy = 75%
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PresetShadowVal) is located in
§A.4.1. end note]
20.1.10.53 ST_RectAlignment (Rectangle Alignments)
This simple type describes how to position two rectangles relative to each other.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
b (Rectangle Alignment Enum ( Bottom )) Bottom
bl (Rectangle Alignment Enum ( Bottom Left )) Bottom Left
br (Rectangle Alignment Enum ( Bottom Right )) Bottom Right
ctr (Rectangle Alignment Enum ( Center )) Center
l (Rectangle Alignment Enum ( Left )) Left
r (Rectangle Alignment Enum ( Right )) Right
t (Rectangle Alignment Enum ( Top )) Top
tl (Rectangle Alignment Enum ( Top Left )) Top Left
tr (Rectangle Alignment Enum ( Top Right )) Top Right
[Note: The W3C XML Schema definition of this simple type’s content model (ST_RectAlignment) is located in
§A.4.1. end note]
20.1.10.54 ST_SchemeColorVal (Scheme Color)
This simple type represents a scheme color value.
©ISO/IEC 2016 – All rights reserved 2987\n\n--- Page 2998 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
accent1 (Accent Color 1) Extra scheme color 1
accent2 (Accent Color 2) Extra scheme color 2
accent3 (Accent Color 3) Extra scheme color 3
accent4 (Accent Color 4) Extra scheme color 4
accent5 (Accent Color 5) Extra scheme color 5
accent6 (Accent Color 6) Extra scheme color 6
bg1 (Background Color 1) Semantic background color
bg2 (Background Color 2) Semantic additional background color
dk1 (Dark Color 1) Main dark color 1
dk2 (Dark Color 2) Main dark color 2
folHlink (Followed Hyperlink Color) Followed Hyperlink Color
hlink (Hyperlink Color) Regular Hyperlink Color
lt1 (Light Color 1) Main Light Color 1
lt2 (Light Color 2) Main Light Color 2
phClr (Style Color) A color used in theme definitions which means to use
the color of the style.
tx1 (Text Color 1) Semantic text color
tx2 (Text Color 2) Semantic additional text color
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SchemeColorVal) is located in
§A.4.1. end note]
20.1.10.55 ST_ShapeID (Shape ID)
Specifies the shape ID for legacy shape identification purposes.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_ShapeID) is located in §A.4.1.
end note]
20.1.10.56 ST_ShapeType (Preset Shape Types)
This simple type specifies the preset shape geometry that is to be used for a shape. An enumeration of this
simple type is used so that a custom geometry does not have to be specified but instead can be constructed
automatically by the generating application. For each enumeration listed there is also the corresponding
DrawingML code that would be used to construct this shape were it a custom geometry. Within the construction
2988 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2999 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
code for each of these preset shapes there are predefined guides that the generating application shall maintain
for calculation purposes at all times. The necessary guides should have the following values. Formula syntax
components are defined in the fmla attribute of the gd element (§20.1.9.11).
3/4 of a Circle ('3cd4') - Constant value of "16200000.0"
The units here are in 60,000ths of a degree. This is equivalent to 270 degrees.
3/8 of a Circle ('3cd8') - Constant value of "8100000.0"
The units here are in 60,000ths of a degree. This is equivalent to 135 degrees.
5/8 of a Circle ('5cd8') - Constant value of "13500000.0"
The units here are in 60,000ths of a degree. This is equivalent to 225 degrees.
7/8 of a Circle ('7cd8') - Constant value of "18900000.0"
The units here are in 60,000ths of a degree. This is equivalent to 315 degrees.
Shape Bottom Edge ('b') - Constant value of "h"
This is the bottom edge of the shape and since the top edge of the shape is considered the 0 point, the
bottom edge is thus the shape height.
1/2 of a Circle ('cd2') - Constant value of "10800000.0"
The units here are in 60,000ths of a degree. This is equivalent to 180 degrees.
1/4 of a Circle ('cd4') - Constant value of "5400000.0"
The units here are in 60,000ths of a degree. This is equivalent to 90 degrees.
1/8 of a Circle ('cd8') - Constant value of "2700000.0"
The units here are in 60,000ths of a degree. This is equivalent to 45 degrees.
Shape Height ('h')
This is the variable height of the shape defined in the shape properties. This value is received from the shape
transform listed within the <spPr> element.
Horizontal Center ('hc') - Calculated value of "*/ w 1.0 2.0"
This is the horizontal center of the shape which is just the width divided by 2.
1/2 of Shape Height ('hd2') - Calculated value of "*/ h 1.0 2.0"
This is 1/2 the shape height.
1/3 of Shape Height ('hd3') - Calculated value of "*/ h 1.0 3.0"
This is 1/3 the shape height.
1/4 of Shape Height ('hd4') - Calculated value of "*/ h 1.0 4.0"
This is 1/4 the shape height.
1/5 of Shape Height ('hd5') - Calculated value of "*/ h 1.0 5.0"
This is 1/5 the shape height.
1/6 of Shape Height ('hd6') - Calculated value of "*/ h 1.0 6.0"
This is 1/6 the shape height.
1/8 of Shape Height ('hd8') - Calculated value of "*/ h 1.0 8.0"
This is 1/8 the shape height.
©ISO/IEC 2016 – All rights reserved 2989\n\n--- Page 3000 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Shape Left Edge ('l') - Constant value of "0"
This is the left edge of the shape and the left edge of the shape is considered the horizontal 0 point.
Longest Side of Shape ('ls') - Calculated value of "max w h"
This is the longest side of the shape. This value is either the width or the height depending on which is greater.
Shape Right Edge ('r') - Constant value of "w"
This is the right edge of the shape and since the left edge of the shape is considered the 0 point, the right edge
is thus the shape width.
Shortest Side of Shape ('ss') - Calculated value of "min w h"
This is the shortest side of the shape. This value is either the width or the height depending on which is
smaller.
1/2 Shortest Side of Shape ('ssd2') - Calculated value of "*/ ss 1.0 2.0"
This is 1/2 the shortest side of the shape.
1/4 Shortest Side of Shape ('ssd4') - Calculated value of "*/ ss 1.0 4.0"
This is 1/4 the shortest side of the shape.
1/6 Shortest Side of Shape ('ssd6') - Calculated value of "*/ ss 1.0 6.0"
This is 1/6 the shortest side of the shape.
1/8 Shortest Side of Shape ('ssd8') - Calculated value of "*/ ss 1.0 8.0"
This is 1/8 the shortest side of the shape.
1/16 Shortest Side of Shape ('ssd16') - Calculated value of "*/ ss 1.0 16.0"
This is 1/16 the shortest side of the shape.
1/32 Shortest Side of Shape ('ssd32') - Calculated value of "*/ ss 1.0 32.0"
This is 1/32 the shortest side of the shape.
Shape Top Edge ('t') - Constant value of "0"
This is the top edge of the shape and the top edge of the shape is considered the vertical 0 point.
Vertical Center of Shape ('vc') - Calculated value of "*/ h 1.0 2.0"
This is the vertical center of the shape which is just the height divided by 2.
Shape Width ('w')
This is the variable width of the shape defined in the shape properties. This value is received from the shape
transform listed within the <spPr> element.
1/2 of Shape Width ('wd2') - Calculated value of "*/ w 1.0 2.0"
This is 1/2 the shape width.
1/3 of Shape Width ('wd3') - Calculated value of "*/ w 1.0 3.0"
This is 1/3 the shape width.
1/4 of Shape Width ('wd4') - Calculated value of "*/ w 1.0 4.0"
This is 1/4 the shape width.
1/5 of Shape Width ('wd5') - Calculated value of "*/ w 1.0 5.0"
2990 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3001 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This is 1/5 the shape width.
1/6 of Shape Width ('wd6') - Calculated value of "*/ w 1.0 6.0"
This is 1/6 the shape width.
1/8 of Shape Width ('wd8') - Calculated value of "*/ w 1.0 8.0"
This is 1/8 the shape width.
1/10 of Shape Width ('wd10') - Calculated value of "*/ w 1.0 10.0"
This is 1/10 the shape width.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
accentBorderCallout1 (Callout 1 with Border and Specifies a preset shape geometry. This geometry shall
Accent Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentBorderCallout1 element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
accentBorderCallout2 (Callout 2 with Border and Specifies a preset shape geometry. This geometry shall
Accent Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentBorderCallout2 element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
accentBorderCallout3 (Callout 3 with Border and Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 2991\n\n--- Page 3002 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
Accent Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentBorderCallout3 element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
accentCallout1 (Callout 1 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentCallout1 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
accentCallout2 (Callout 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentCallout2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
2992 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3003 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
accentCallout3 (Callout 3 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the accentCallout3 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonBackPrevious (Back or Previous Button Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonBackPrevious element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonBeginning (Beginning Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonBeginning element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
©ISO/IEC 2016 – All rights reserved 2993\n\n--- Page 3004 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
actionButtonBlank (Blank Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonBlank element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonDocument (Document Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonDocument element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonEnd (End Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
2994 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3005 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the actionButtonEnd element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonForwardNext (Forward or Next Button Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonForwardNext element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonHelp (Help Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonHelp element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
©ISO/IEC 2016 – All rights reserved 2995\n\n--- Page 3006 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
actionButtonHome (Home Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonHome element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonInformation (Information Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonInformation element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonMovie (Movie Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonMovie element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
2996 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3007 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
actionButtonReturn (Return Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonReturn element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
actionButtonSound (Sound Button Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the actionButtonSound element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
arc (Curved Arc Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
©ISO/IEC 2016 – All rights reserved 2997\n\n--- Page 3008 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the arc element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
bentArrow (Bent Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bentArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bentConnector2 (Bent Connector 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bentConnector2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bentConnector3 (Bent Connector 3 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
2998 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3009 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the bentConnector3 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bentConnector4 (Bent Connector 4 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bentConnector4 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bentConnector5 (Bent Connector 5 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bentConnector5 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bentUpArrow (Bent Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
©ISO/IEC 2016 – All rights reserved 2999\n\n--- Page 3010 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bentUpArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
bevel (Bevel Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bevel element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
blockArc (Block Arc Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the blockArc element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
borderCallout1 (Callout 1 with Border Shape) Specifies a preset shape geometry. This geometry shall
3000 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3011 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the borderCallout1 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
borderCallout2 (Callout 2 with Border Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the borderCallout2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
borderCallout3 (Callout 3 with Border Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the borderCallout3 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
©ISO/IEC 2016 – All rights reserved 3001\n\n--- Page 3012 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
bracePair (Brace Pair Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bracePair element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
bracketPair (Bracket Pair Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the bracketPair element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
callout1 (Callout 1 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the callout1 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
3002 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3013 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
callout2 (Callout 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the callout2 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
callout3 (Callout 3 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the callout3 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
can (Can Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the can element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3003\n\n--- Page 3014 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
chartPlus (Chart Plus Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the chartPlus element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
chartStar (Chart Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the chartStar element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
chartX (Chart X Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the chartX element in the preset shape geometries
3004 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3015 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
chevron (Chevron Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the chevron element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
chord (Chord Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the chord element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
circularArrow (Circular Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
©ISO/IEC 2016 – All rights reserved 3005\n\n--- Page 3016 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the circularArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
cloud (Cloud Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the cloud element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
cloudCallout (Callout Cloud Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the cloudCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
corner (Corner Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
3006 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3017 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the corner element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
cornerTabs (Corner Tabs Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the cornerTabs element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
cube (Cube Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the cube element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
curvedConnector2 (Curved Connector 2 Shape) Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 3007\n\n--- Page 3018 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedConnector2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
curvedConnector3 (Curved Connector 3 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedConnector3 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
curvedConnector4 (Curved Connector 4 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedConnector4 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
3008 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3019 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
curvedConnector5 (Curved Connector 5 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedConnector5 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
curvedDownArrow (Curved Down Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedDownArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
curvedLeftArrow (Curved Left Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedLeftArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
©ISO/IEC 2016 – All rights reserved 3009\n\n--- Page 3020 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
curvedRightArrow (Curved Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedRightArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
curvedUpArrow (Curved Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the curvedUpArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
decagon (Decagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
3010 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3021 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the decagon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
diagStripe (Diagonal Stripe Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the diagStripe element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
diamond (Diamond Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the diamond element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3011\n\n--- Page 3022 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
dodecagon (Dodecagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the dodecagon element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
donut (Donut Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the donut element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
doubleWave (Double Wave Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the doubleWave element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
3012 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3023 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
downArrow (Down Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the downArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
downArrowCallout (Callout Down Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the downArrowCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
ellipse (Ellipse Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the ellipse element in the preset shape geometries
©ISO/IEC 2016 – All rights reserved 3013\n\n--- Page 3024 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
ellipseRibbon (Ellipse Ribbon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the ellipseRibbon element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
ellipseRibbon2 (Ellipse Ribbon 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the ellipseRibbon2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartAlternateProcess (Alternate Process Flow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
3014 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3025 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartAlternateProcess element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartCollate (Collate Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartCollate element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartConnector (Connector Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartConnector element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartDecision (Decision Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
©ISO/IEC 2016 – All rights reserved 3015\n\n--- Page 3026 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartDecision element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartDelay (Delay Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartDelay element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartDisplay (Display Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartDisplay element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartDocument (Document Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
3016 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3027 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartDocument element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartExtract (Extract Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartExtract element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartInputOutput (Input Output Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartInputOutput element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartInternalStorage (Internal Storage Flow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
©ISO/IEC 2016 – All rights reserved 3017\n\n--- Page 3028 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartInternalStorage element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartMagneticDisk (Magnetic Disk Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartMegneticDisk element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartMagneticDrum (Magnetic Drum Flow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartMagneticDrum element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartMagneticTape (Magnetic Tape Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
3018 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3029 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartMagneticTape element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartManualInput (Manual Input Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartManualInput element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartManualOperation (Manual Operation Flow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartManualOperation element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartMerge (Merge Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
©ISO/IEC 2016 – All rights reserved 3019\n\n--- Page 3030 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the flowChartMerge element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartMultidocument (Multi-Document Flow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartMultidocument element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartOfflineStorage (Offline Storage Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartOfflineStorage element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartOffpageConnector (Off-Page Connector Specifies a preset shape geometry. This geometry shall
Flow Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
3020 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3031 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartOffpageConnector element in the
preset shape geometries electronic addenda of Annex
D. The constants used in that markup are guides that
are described in further detail above. end note]
flowChartOnlineStorage (Online Storage Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartOnlineStorage element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartOr (Or Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartOr element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartPredefinedProcess (Predefined Process Specifies a preset shape geometry. This geometry shall
Flow Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
©ISO/IEC 2016 – All rights reserved 3021\n\n--- Page 3032 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartPredefinedProcess element in the
preset shape geometries electronic addenda of Annex
D. The constants used in that markup are guides that
are described in further detail above. end note]
flowChartPreparation (Preparation Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartPreparation element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartProcess (Process Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartProcess element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartPunchedCard (Punched Card Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
3022 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3033 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the flowChartPunchedCard element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartPunchedTape (Punched Tape Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartPunchedTape element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartSort (Sort Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartSort element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
flowChartSummingJunction (Summing Junction Flow Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 3023\n\n--- Page 3034 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartSummingJunction element in the
preset shape geometries electronic addenda of Annex
D. The constants used in that markup are guides that
are described in further detail above. end note]
flowChartTerminator (Terminator Flow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the flowChartTerminator element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
foldedCorner (Folded Corner Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the foldedCorner element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
frame (Frame Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3024 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3035 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the frame element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
funnel (Funnel Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the funnel element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
gear6 (Gear 6 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the gear6 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
gear9 (Gear 9 Shape) Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 3025\n\n--- Page 3036 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the gear9 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
halfFrame (Half Frame Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the halfFrame element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
heart (Heart Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the heart element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
3026 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3037 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
heptagon (Heptagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the heptagon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
hexagon (Hexagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the hexagon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
homePlate (Home Plate Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
©ISO/IEC 2016 – All rights reserved 3027\n\n--- Page 3038 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the homePlate element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
horizontalScroll (Horizontal Scroll Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the horizontalScroll element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
irregularSeal1 (Irregular Seal 1 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the irregularSeal1 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
irregularSeal2 (Irregular Seal 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3028 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3039 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the irregularSeal2 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftArrow (Left Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftArrow element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
leftArrowCallout (Callout Left Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftArrowCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftBrace (Left Brace Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
©ISO/IEC 2016 – All rights reserved 3029\n\n--- Page 3040 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftBrace element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
leftBracket (Left Bracket Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftBracket element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftCircularArrow (Left Circular Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftCircularArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftRightArrow (Left Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
3030 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3041 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftRightArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftRightArrowCallout (Callout Left Right Arrow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftRightArrowCallout element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftRightCircularArrow (Left Right Circular Arrow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftRightCircularArrow element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftRightRibbon (Left Right Ribbon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
©ISO/IEC 2016 – All rights reserved 3031\n\n--- Page 3042 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
generate this preset shape definition is contained in
the leftRightRibbon element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftRightUpArrow (Left Right Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftRightUpArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
leftUpArrow (Left Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the leftUpArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
lightningBolt (Lightning Bolt Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3032 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3043 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the lightningBolt element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
line (Line Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the line element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
lineInv (Line Inverse Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the lineInv element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3033\n\n--- Page 3044 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
mathDivide (Divide Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathDivide element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
mathEqual (Equal Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathEqual element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
mathMinus (Minus Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathMinus element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
mathMultiply (Multiply Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3034 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3045 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathMultiply element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
mathNotEqual (Not Equal Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathNotEqual element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
mathPlus (Plus Math Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the mathPlus element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
moon (Moon Shape) Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 3035\n\n--- Page 3046 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the moon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
nonIsoscelesTrapezoid (Non-Isosceles Trapezoid Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the nonIsocelesTrapezoid element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
noSmoking (No Smoking Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the noSmoking element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
3036 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3047 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
notchedRightArrow (Notched Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the notchedRightArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
octagon (Octagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the octagon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
parallelogram (Parallelogram Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the parallelogram element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
©ISO/IEC 2016 – All rights reserved 3037\n\n--- Page 3048 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
described in further detail above. end note]
pentagon (Pentagon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the pentagon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
pie (Pie Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the pie element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
pieWedge (Pie Wedge Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3038 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3049 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the pieWedge element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
plaque (Plaque Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the plaque element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
plaqueTabs (Plaque Tabs Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the plaqueTabs element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
plus (Plus Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
©ISO/IEC 2016 – All rights reserved 3039\n\n--- Page 3050 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the plus element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
quadArrow (Quad-Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the quadArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
quadArrowCallout (Callout Quad-Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the quadArrowCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
3040 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3051 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
rect (Rectangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the rect element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
ribbon (Ribbon Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the ribbon element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
ribbon2 (Ribbon 2 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the ribbon2 element in the preset shape geometries
©ISO/IEC 2016 – All rights reserved 3041\n\n--- Page 3052 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
rightArrow (Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the rightArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
rightArrowCallout (Callout Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the rightArrowCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
rightBrace (Right Brace Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
3042 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3053 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the rightBrace element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
rightBracket (Right Bracket Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the rightBracket element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
round1Rect (One Round Corner Rectangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the round1Rect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
round2DiagRect (Two Diagonal Round Corner Specifies a preset shape geometry. This geometry shall
Rectangle Shape) be designed to match the normative image below.
©ISO/IEC 2016 – All rights reserved 3043\n\n--- Page 3054 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the round2DiagRect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
round2SameRect (Two Same-side Round Corner Specifies a preset shape geometry. This geometry shall
Rectangle Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the round2SameRect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
roundRect (Round Corner Rectangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the roundRect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
rtTriangle (Right Triangle Shape) Specifies a preset shape geometry. This geometry shall
3044 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3055 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the rtTriangle element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
smileyFace (Smiley Face Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the smileyFace element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
snip1Rect (One Snip Corner Rectangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the snip1Rect element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3045\n\n--- Page 3056 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
snip2DiagRect (Two Diagonal Snip Corner Rectangle Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the snip2DiagRect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
snip2SameRect (Two Same-side Snip Corner Specifies a preset shape geometry. This geometry shall
Rectangle Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the snip2SameRect element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
snipRoundRect (One Snip One Round Corner Specifies a preset shape geometry. This geometry shall
Rectangle Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the snipRoundRect element in the preset shape
geometries electronic addenda of Annex D. The
3046 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3057 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
constants used in that markup are guides that are
described in further detail above. end note]
squareTabs (Square Tabs Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the squareTabs element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
star10 (Ten Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star10 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star12 (Twelve Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
©ISO/IEC 2016 – All rights reserved 3047\n\n--- Page 3058 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the star12 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star16 (Sixteen Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star16 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star24 (Twenty Four Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star24 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star32 (Thirty Two Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3048 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3059 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star32 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star4 (Four Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star4 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star5 (Five Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star5 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3049\n\n--- Page 3060 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
star6 (Six Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star6 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star7 (Seven Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star7 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
star8 (Eight Pointed Star Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the star8 element in the preset shape geometries
electronic addenda of Annex D. The constants used in
3050 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3061 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
that markup are guides that are described in further
detail above. end note]
straightConnector1 (Straight Connector 1 Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the straightConnector1 element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
stripedRightArrow (Striped Right Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the stripedRightArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
sun (Sun Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
©ISO/IEC 2016 – All rights reserved 3051\n\n--- Page 3062 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the sun element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
swooshArrow (Swoosh Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the swooshArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
teardrop (Teardrop Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the teardrop element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
trapezoid (Trapezoid Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
3052 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3063 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the trapezoid element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
triangle (Triangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the triangle element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
upArrow (Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the upArrow element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3053\n\n--- Page 3064 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
upArrowCallout (Callout Up Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the upArrowCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
upDownArrow (Up Down Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the upDownArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
upDownArrowCallout (Callout Up Down Arrow Specifies a preset shape geometry. This geometry shall
Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
3054 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3065 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
the upDownArrowCallout element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
uturnArrow (U-Turn Arrow Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the uturnArrow element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
verticalScroll (Vertical Scroll Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the verticalScroll element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
wave (Wave Shape) Specifies a preset shape geometry. This geometry shall
©ISO/IEC 2016 – All rights reserved 3055\n\n--- Page 3066 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the wave element in the preset shape geometries
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
wedgeEllipseCallout (Callout Wedge Ellipse Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the wedgeEllipseCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
wedgeRectCallout (Callout Wedge Rectangle Shape) Specifies a preset shape geometry. This geometry shall
be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the wedgeRectCallout element in the preset shape
geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
3056 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3067 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
wedgeRoundRectCallout (Callout Wedge Round Specifies a preset shape geometry. This geometry shall
Rectangle Shape) be designed to match the normative image below.
[Note: An example of DrawingML which can be used to
generate this preset shape definition is contained in
the wedgeRoundRectCallout element in the preset
shape geometries electronic addenda of Annex D. The
constants used in that markup are guides that are
described in further detail above. end note]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_ShapeType) is located in §A.4.1.
end note]
20.1.10.57 ST_StyleMatrixColumnIndex (Style Matrix Column Index)
This simple type specifies an index into one of the lists in the style matrix specified by the fmtScheme element
(bgFillStyleLst, effectStyleLst, fillStyleLst, or lnStyleLst).
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_StyleMatrixColumnIndex) is
located in §A.4.1. end note]
20.1.10.58 ST_SystemColorVal (System Color Value)
This simple type specifies a system color value. This color is based upon the value that this color currently has
within the system on which the document is being viewed.
Applications shall use the lastClr attribute to determine the absolute value of the last color used if system colors
are not supported.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 3057\n\n--- Page 3068 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
3dDkShadow (3D Dark System Color) Specifies a Dark shadow color for three-dimensional
display elements.
3dLight (3D Light System Color) Specifies a Light color for three-dimensional display
elements (for edges facing the light source).
activeBorder (Active Border System Color) Specifies an Active Window Border Color.
activeCaption (Active Caption System Color) Specifies the active window title bar color. In particular
the left side color in the color gradient of an active
window's title bar if the gradient effect is enabled.
appWorkspace (Application Workspace System Color) Specifies the Background color of multiple document
interface (MDI) applications.
background (Background System Color) Specifies the desktop background color.
btnFace (Button Face System Color) Specifies the face color for three-dimensional display
elements and for dialog box backgrounds.
btnHighlight (Button Highlight System Color) Specifies the highlight color for three-dimensional
display elements (for edges facing the light source).
btnShadow (Button Shadow System Color) Specifies the shadow color for three-dimensional
display elements (for edges facing away from the light
source).
btnText (Button Text System Color) Specifies the color of text on push buttons.
captionText (Caption Text System Color) Specifies the color of text in the caption, size box, and
scroll bar arrow box.
gradientActiveCaption (Gradient Active Caption Specifies the right side color in the color gradient of an
System Color) active window's title bar.
gradientInactiveCaption (Gradient Inactive Caption Specifies the right side color in the color gradient of an
System Color) inactive window's title bar.
grayText (Gray Text System Color) Specifies a grayed (disabled) text. This color is set to 0
if the current display driver does not support a solid
gray color.
highlight (Highlight System Color) Specifies the color of Item(s) selected in a control.
highlightText (Highlight Text System Color) Specifies the text color of item(s) selected in a control.
hotLight (Hot Light System Color) Specifies the color for a hyperlink or hot-tracked item.
inactiveBorder (Inactive Border System Color) Specifies the color of the Inactive window border.
inactiveCaption (Inactive Caption System Color) Specifies the color of the Inactive window caption.
Specifies the left side color in the color gradient of an
inactive window's title bar if the gradient effect is
enabled.
inactiveCaptionText (Inactive Caption Text System Specifies the color of text in an inactive caption.
Color)
3058 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3069 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
infoBk (Info Back System Color) Specifies the background color for tooltip controls.
infoText (Info Text System Color) Specifies the text color for tooltip controls.
menu (Menu System Color) Specifies the menu background color.
menuBar (Menu Bar System Color) Specifies the background color for the menu bar when
menus appear as flat menus.
menuHighlight (Menu Highlight System Color) Specifies the color used to highlight menu items when
the menu appears as a flat menu.
menuText (Menu Text System Color) Specifies the color of Text in menus.
scrollBar (Scroll Bar System Color) Specifies the scroll bar gray area color.
window (Window System Color) Specifies window background color.
windowFrame (Window Frame System Color) Specifies the window frame color.
windowText (Window Text System Color) Specifies the color of text in windows.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SystemColorVal) is located in
§A.4.1. end note]
20.1.10.59 ST_TextAlignType (Text Alignment Types)
This simple type specifies the text alignment types
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
ctr (Text Alignment Enum ( Center )) Align text in the center.
dist (Text Alignment Enum ( Distributed )) Distributes the text words across an entire text line.
just (Text Alignment Enum ( Justified )) Align text so that it is justified across the whole line. It
is smart in the sense that it does not justify sentences
which are short.
justLow (Text Alignment Enum ( Justified Low )) Aligns the text with an adjusted kashida length for
Arabic text.
l (Text Alignment Enum ( Left )) Align text to the left margin.
r (Text Alignment Enum ( Right )) Align text to the right margin.
thaiDist (Text Alignment Enum ( Thai Distributed )) Distributes Thai text specially, because each character
is treated as a word.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextAlignType) is located in
§A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 3059\n\n--- Page 3070 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.60 ST_TextAnchoringType (Text Anchoring Types)
This simple type specifies a list of available anchoring types for text.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
b (Text Anchor Enum ( Bottom )) Anchor the text at the bottom of the bounding
rectangle.
ctr (Text Anchor Enum ( Center )) Anchor the text at the middle of the bounding
rectangle.
dist (Text Anchor Enum ( Distributed )) Anchor the text so that it is distributed vertically.
When text is horizontal, this spaces out the actual lines
of text and is almost always identical in behavior to
anchorJustified (special case: if only 1 line, then
anchored in middle). When text is vertical, then it
distributes the letters vertically. This is different than
anchorJustified, because it always forces distribution
of the words, even if there are only one or two words
in a line.
just (Text Anchor Enum ( Justified )) Anchor the text so that it is justified vertically. When
text is horizontal, this spaces out the actual lines of
text and is almost always identical in behavior to
'distrib' (special case: if only 1 line, then anchored at
top). When text is vertical, then it justifies the letters
vertically. This is different than anchorDistributed,
because in some cases such as very little text in a line,
it does not justify.
t (Text Anchoring Type Enum ( Top )) Anchor the text at the top of the bounding rectangle.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextAnchoringType) is located in
§A.4.1. end note]
20.1.10.61 ST_TextAutonumberScheme (Text Auto-number Schemes)
This simple type specifies a list of automatic numbering schemes.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
alphaLcParenBoth (Autonumber Enum ( (a), (b), (c), …
alphaLcParenBoth ))
3060 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3071 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
alphaLcParenR (Autonumbering Enum ( a), b), c), …
alphaLcParenR ))
alphaLcPeriod (Autonumbering Enum ( alphaLcPeriod a., b., c., …
))
alphaUcParenBoth (Autonumbering Enum ( (A), (B), (C), …
alphaUcParenBoth ))
alphaUcParenR (Autonumbering Enum ( A), B), C), …
alphaUcParenR ))
alphaUcPeriod (Autonumbering Enum ( A., B., C., …
alphaUcPeriod ))
arabic1Minus (Autonumbering Enum ( arabic1Minus Bidi Arabic 1 (AraAlpha) with ANSI minus symbol
))
arabic2Minus (Autonumbering Enum ( arabic2Minus Bidi Arabic 2 (AraAbjad) with ANSI minus symbol
))
arabicDbPeriod (Autonumbering Enum ( Dbl-byte Arabic numbers w/ double-byte period
arabicDbPeriod ))
arabicDbPlain (Autonumbering Enum ( arabicDbPlain Dbl-byte Arabic numbers
))
arabicParenBoth (Autonumbering Enum ( (1), (2), (3), …
arabicParenBoth ))
arabicParenR (Autonumbering Enum ( arabicParenR )) 1), 2), 3), …
arabicPeriod (Autonumbering Enum ( arabicPeriod )) 1., 2., 3., …
arabicPlain (Autonumbering Enum ( arabicPlain )) 1, 2, 3, …
circleNumDbPlain (Autonumbering Enum ( Dbl-byte circle numbers (1-10 circle[0x2460-], 11-
circleNumDbPlain )) arabic numbers)
circleNumWdBlackPlain (Autonumbering Enum ( Wingdings black circle numbers
circleNumWdBlackPlain ))
circleNumWdWhitePlain (Autonumbering Enum ( Wingdings white circle numbers (0-10 circle[0x0080-],
circleNumWdWhitePlain )) 11- arabic numbers)
ea1ChsPeriod (Autonumbering Enum ( ea1ChsPeriod EA: Simplified Chinese w/ single-byte period
))
ea1ChsPlain (Autonumbering Enum ( ea1ChsPlain )) EA: Simplified Chinese (TypeA 1-99, TypeC 100-)
ea1ChtPeriod (Autonumbering Enum ( ea1ChtPeriod EA: Traditional Chinese w/ single-byte period
))
ea1ChtPlain (Autonumbering Enum ( ea1ChtPlain )) EA: Traditional Chinese (TypeA 1-19, TypeC 20-)
ea1JpnChsDbPeriod (Autonumbering Enum ( EA: Japanese w/ double-byte period
ea1JpnChsDbPeriod ))
ea1JpnKorPeriod (Autonumbering Enum ( EA: Japanese/Korean w/ single-byte period
©ISO/IEC 2016 – All rights reserved 3061\n\n--- Page 3072 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
ea1JpnKorPeriod ))
ea1JpnKorPlain (Autonumbering Enum ( EA: Japanese/Korean (TypeC 1-)
ea1JpnKorPlain ))
hebrew2Minus (Autonumbering Enum ( Bidi Hebrew 2 with ANSI minus symbol
hebrew2Minus ))
hindiAlpha1Period (Autonumbering Enum ( Hindi alphabet period - consonants
hindiAlpha1Period ))
hindiAlphaPeriod (Autonumbering Enum ( Hindi alphabet period - vowels
hindiAlphaPeriod ))
hindiNumParenR (Autonumbering Enum ( Hindi numerical parentheses - right
hindiNumParenR ))
hindiNumPeriod (Autonumbering Enum ( Hindi numerical period
hindiNumPeriod ))
romanLcParenBoth (Autonumbering Enum ( (i), (ii), (iii), …
romanLcParenBoth ))
romanLcParenR (Autonumbering Enum ( i), ii), iii), …
romanLcParenR ))
romanLcPeriod (Autonumbering Enum ( i., ii., iii., …
romanLcPeriod ))
romanUcParenBoth (Autonumbering Enum ( (I), (II), (III), …
romanUcParenBoth ))
romanUcParenR (Autonumbering Enum ( I), II), III), …
romanUcParenR ))
romanUcPeriod (Autonumbering Enum ( I., II., III., …
romanUcPeriod ))
thaiAlphaParenBoth (Autonumbering Enum ( Thai alphabet parentheses - both
thaiAlphaParenBoth ))
thaiAlphaParenR (Autonumbering Enum ( Thai alphabet parentheses - right
thaiAlphaParenR ))
thaiAlphaPeriod (Autonumbering Enum ( Thai alphabet period
thaiAlphaPeriod ))
thaiNumParenBoth (Autonumbering Enum ( Thai numerical parentheses - both
thaiNumParenBoth ))
thaiNumParenR (Autonumbering Enum ( Thai numerical parentheses - right
thaiNumParenR ))
thaiNumPeriod (Autonumbering Enum ( Thai numerical period
thaiNumPeriod ))
3062 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3073 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextAutonumberScheme) is
located in §A.4.1. end note]
20.1.10.62 ST_TextBulletSizePercent (Bullet Size Percentage)
This simple type specifies the range that the bullet percent can be. A bullet percent is the size of the bullet with
respect to the text that should follow it.
This simple type also specifies the following restrictions:
 This simple type’s contents shall match the following regular expression pattern:
0*((2[5-9])|([3-9][0-9])|([1-3][0-9][0-9])|400)%.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextBulletSizePercent) is located
in §A.4.1. end note]
20.1.10.63 ST_TextBulletStartAtNum (Start Bullet At Number)
This simple type specifies the range that the start at number for a bullet's auto-numbering sequence can begin
at. When the numbering is alphabetical, then the numbers map to the appropriate letter. 1->a, 2->b, etc. If the
numbers go above 26, then the numbers begin to double up. For example, 27->aa and 53->aaa.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 1.
 This simple type has a maximum value of less than or equal to 32767.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextBulletStartAtNum) is
located in §A.4.1. end note]
20.1.10.64 ST_TextCapsType (Text Cap Types)
This simple type specifies the cap types of the text.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
all (Text Caps Enum ( All )) Apply all caps on the text. All lower case letters are
converted to upper case even though they are stored
differently in the backing store.
none (Text Caps Enum ( None )) The reason we cannot implicitly have noCaps be the
scenario where capitalization is not specified is
because not being specified implies deriving from a
particular style and the user might want to override
that and make some text not have a capitalization
©ISO/IEC 2016 – All rights reserved 3063\n\n--- Page 3074 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
scheme even though the style says otherwise.
small (Text Caps Enum ( Small )) Apply small caps to the text. All letters are converted
to lower case.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextCapsType) is located in
§A.4.1. end note]
20.1.10.65 ST_TextColumnCount (Text Column Count)
This simple type specifies the number of columns.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 1.
 This simple type has a maximum value of less than or equal to 16.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextColumnCount) is located in
§A.4.1. end note]
20.1.10.66 ST_TextFontAlignType (Font Alignment Types)
This simple type specifies the different kinds of font alignment.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
auto (Font Alignment Enum ( Automatic )) When the text flow is horizontal or simple vertical
same as fontBaseline but for other vertical modes
same as fontCenter.
b (Font Alignment Enum ( Bottom )) The letters are anchored to the very bottom of a single
line. This is different than the bottom baseline because
of letters such as "g," "q," "y," etc.
base (Font Alignment Enum ( Baseline )) The letters are anchored to the bottom baseline of a
single line.
ctr (Font Alignment Enum ( Center )) The letters are anchored between the two baselines of
a single line.
t (Font Alignment Enum ( Top )) The letters are anchored to the top baseline of a single
line.
3064 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3075 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextFontAlignType) is located in
§A.4.1. end note]
20.1.10.67 ST_TextFontScalePercentOrPercentString (Text Font Scale Percentage)
This simple type specifies that its contents will contain a text font scale percent percentage. See the union's
member types for details.
This simple type is a union of the following types:
 The ST_Percentage simple type (§22.9.2.9).
[Note: The W3C XML Schema definition of this simple type’s content model
(ST_TextFontScalePercentOrPercentString) is located in §A.4.1. end note]
20.1.10.68 ST_TextFontSize (Text Font Size)
This simple type specifies the size of any text in hundredths of a point. Shall be at least 1 point.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 100.
 This simple type has a maximum value of less than or equal to 400000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextFontSize) is located in
§A.4.1. end note]
20.1.10.69 ST_TextHorzOverflowType (Text Horizontal Overflow Types)
This simple type specifies the text horizontal overflow types
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
clip (Text Horizontal Overflow Enum ( Clip )) When a big character does not fit into a line, clip it at
the proper horizontal overflow.
overflow (Text Horizontal Overflow Enum ( Overflow When a big character does not fit into a line, allow a
)) horizontal overflow.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextHorzOverflowType) is
located in §A.4.1. end note]
20.1.10.70 ST_TextIndent (Text Indentation)
This simple type specifies the text indentation amount to be used.
©ISO/IEC 2016 – All rights reserved 3065\n\n--- Page 3076 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The units of measurement used here are EMUs (English Metric Units).
This simple type's contents are a restriction of the ST_Coordinate32Unqualified datatype (§20.1.10.18).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to -51206400.
 This simple type has a maximum value of less than or equal to 51206400.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextIndent) is located in §A.4.1.
end note]
20.1.10.71 ST_TextIndentLevelType (Text Indent Level Type)
This simple type specifies the indent level type. We support list level 0 to 8, and we use -1 and -2 for outline
mode levels that should only exist in memory.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 8.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextIndentLevelType) is located
in §A.4.1. end note]
20.1.10.72 ST_TextMargin (Text Margin)
This simple type specifies the margin that is used and its corresponding size.
This simple type's contents are a restriction of the ST_Coordinate32Unqualified datatype (§20.1.10.18).
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 51206400.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextMargin) is located in §A.4.1.
end note]
20.1.10.73 ST_TextNonNegativePoint (Text Non-Negative Point)
This simple type specifies a non-negative font size in hundredths of a point. This is restricted to the range [0,
400000].
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
3066 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3077 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 This simple type has a minimum value of greater than or equal to 0.
 This simple type has a maximum value of less than or equal to 400000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextNonNegativePoint) is
located in §A.4.1. end note]
20.1.10.74 ST_TextPoint (Text Point)
This simple type specifies a coordinate within the document. This can be used for measurements or spacing; its
maximum size is +/- 4000 points.
Its contents can contain either:
 A whole number, whose contents consist of a measurement in hundredths of a point
 A number immediately followed by a unit identifier
This simple type is a union of the following types:
 The ST_TextPointUnqualified simple type (§20.1.10.75).
 The ST_UniversalMeasure simple type (§22.9.2.15).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextPoint) is located in §A.4.1.
end note]
20.1.10.75 ST_TextPointUnqualified (Text Point)
This simple type specifies a font size in hundredths of a point. This is restricted to the range [-400000, 400000],
i.e from -4000 pt to 4000 pt.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to -400000.
 This simple type has a maximum value of less than or equal to 400000.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextPointUnqualified) is located
in §A.4.1. end note]
20.1.10.76 ST_TextShapeType (Preset Text Shape Types)
This simple type specifies the preset text shape geometry that is to be used for a shape. An enumeration of this
simple type is used so that a custom geometry does not have to be specified but instead can be constructed
automatically by the generating application. For each enumeration listed there is also the corresponding
DrawingML code that would be used to construct this shape were it a custom geometry. Within the construction
code for each of these preset text shapes there are predefined guides that the generating application shall
maintain for calculation purposes at all times. The necessary guides should have the following values. Formula
syntax components are defined in the fmla attribute of the gd element (§20.1.9.11).
©ISO/IEC 2016 – All rights reserved 3067\n\n--- Page 3078 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
3/4 of a Circle ('3cd4') - Constant value of "16200000.0"
The units here are in 60,000ths of a degree. This is equivalent to 270 degrees.
3/8 of a Circle ('3cd8') - Constant value of "8100000.0"
The units here are in 60,000ths of a degree. This is equivalent to 135 degrees.
5/8 of a Circle ('5cd8') - Constant value of "13500000.0"
The units here are in 60,000ths of a degree. This is equivalent to 225 degrees.
7/8 of a Circle ('7cd8') - Constant value of "18900000.0"
The units here are in 60,000ths of a degree. This is equivalent to 315 degrees.
Shape Bottom Edge ('b') - Constant value of "h"
This is the bottom edge of the shape and since the top edge of the shape is considered the 0 point, the
bottom edge is thus the shape height.
1/2 of a Circle ('cd2') - Constant value of "10800000.0"
The units here are in 60,000ths of a degree. This is equivalent to 180 degrees.
1/4 of a Circle ('cd4') - Constant value of "5400000.0"
The units here are in 60,000ths of a degree. This is equivalent to 90 degrees.
1/8 of a Circle ('cd8') - Constant value of "2700000.0"
The units here are in 60,000ths of a degree. This is equivalent to 45 degrees.
Shape Height ('h')
This is the variable height of the shape defined in the shape properties. This value is received from the shape
transform listed within the <spPr> element.
Horizontal Center ('hc') - Calculated value of "*/ w 1.0 2.0"
This is the horizontal center of the shape which is just the width divided by 2.
1/2 of Shape Height ('hd2') - Calculated value of "*/ h 1.0 2.0"
This is 1/2 the shape height.
1/3 of Shape Height ('hd3') - Calculated value of "*/ h 1.0 3.0"
This is 1/3 the shape height.
1/4 of Shape Height ('hd4') - Calculated value of "*/ h 1.0 4.0"
This is 1/4 the shape height.
1/5 of Shape Height ('hd5') - Calculated value of "*/ h 1.0 5.0"
This is 1/5 the shape height.
1/6 of Shape Height ('hd6') - Calculated value of "*/ h 1.0 6.0"
This is 1/6 the shape height.
1/8 of Shape Height ('hd8') - Calculated value of "*/ h 1.0 8.0"
This is 1/8 the shape height.
Shape Left Edge ('l') - Constant value of "0"
This is the left edge of the shape and the left edge of the shape is considered the horizontal 0 point.
Longest Side of Shape ('ls') - Calculated value of "max w h"
3068 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3079 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This is the longest side of the shape. This value is either the width or the height depending on which is greater.
Shape Right Edge ('r') - Constant value of "w"
This is the right edge of the shape and since the left edge of the shape is considered the 0 point, the right edge
is thus the shape width.
Shortest Side of Shape ('ss') - Calculated value of "min w h"
This is the shortest side of the shape. This value is either the width or the height depending on which is
smaller.
1/2 Shortest Side of Shape ('ssd2') - Calculated value of "*/ ss 1.0 2.0"
This is 1/2 the shortest side of the shape.
1/4 Shortest Side of Shape ('ssd4') - Calculated value of "*/ ss 1.0 4.0"
This is 1/4 the shortest side of the shape.
1/6 Shortest Side of Shape ('ssd6') - Calculated value of "*/ ss 1.0 6.0"
This is 1/6 the shortest side of the shape.
1/8 Shortest Side of Shape ('ssd8') - Calculated value of "*/ ss 1.0 8.0"
This is 1/8 the shortest side of the shape.
1/16 Shortest Side of Shape ('ssd16') - Calculated value of "*/ ss 1.0 16.0"
This is 1/16 the shortest side of the shape.
1/32 Shortest Side of Shape ('ssd32') - Calculated value of "*/ ss 1.0 32.0"
This is 1/32 the shortest side of the shape.
Shape Top Edge ('t') - Constant value of "0"
This is the top edge of the shape and the top edge of the shape is considered the vertical 0 point.
Vertical Center of Shape ('vc') - Calculated value of "*/ h 1.0 2.0"
This is the vertical center of the shape which is just the height divided by 2.
Shape Width ('w')
This is the variable width of the shape defined in the shape properties. This value is received from the shape
transform listed within the <spPr> element.
1/2 of Shape Width ('wd2') - Calculated value of "*/ w 1.0 2.0"
This is 1/2 the shape width.
1/3 of Shape Width ('wd3') - Calculated value of "*/ w 1.0 3.0"
This is 1/3 the shape width.
1/4 of Shape Width ('wd4') - Calculated value of "*/ w 1.0 4.0"
This is 1/4 the shape width.
1/5 of Shape Width ('wd5') - Calculated value of "*/ w 1.0 5.0"
This is 1/5 the shape width.
1/6 of Shape Width ('wd6') - Calculated value of "*/ w 1.0 6.0"
This is 1/6 the shape width.
©ISO/IEC 2016 – All rights reserved 3069\n\n--- Page 3080 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
1/8 of Shape Width ('wd8') - Calculated value of "*/ w 1.0 8.0"
This is 1/8 the shape width.
1/10 of Shape Width ('wd10') - Calculated value of "*/ w 1.0 10.0"
This is 1/10 the shape width.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
textArchDown (Downward Arch Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textArchDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textArchDownPour (Downward Pour Arch Text
Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textArchDownPour element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textArchUp (Upward Arch Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textArchUp element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
3070 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3081 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
above. end note]
textArchUpPour (Upward Pour Arch Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textArchUpPour element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textButton (Button Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textButton element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textButtonPour (Button Pour Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textButtonPour element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
©ISO/IEC 2016 – All rights reserved 3071\n\n--- Page 3082 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
textCanDown (Downward Can Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCanDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textCanUp (Upward Can Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCanUp element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textCascadeDown (Downward Cascade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCascadeDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textCascadeUp (Upward Cascade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
3072 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3083 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be used to achieve this effect is contained in the
textCascadeUp element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textChevron (Chevron Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textChevron element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textChevronInverted (Inverted Chevron Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textChevronInverted element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textCircle (Circle Text Shape) Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCircle element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textCirclePour (Circle Pour Text Shape)
©ISO/IEC 2016 – All rights reserved 3073\n\n--- Page 3084 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCirclePour element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textCurveDown (Downward Curve Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCurveDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textCurveUp (Upward Curve Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textCurveUp element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textDeflate (Deflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDeflate element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
3074 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3085 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
above. end note]
textDeflateBottom (Bottom Deflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDeflateBottom element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textDeflateInflate (Deflate-Inflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDeflateInflate element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textDeflateInflateDeflate (Deflate-Inflate-Deflate Text
Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDeflateInflateDeflate element in the preset text
warp electronic addenda of Annex D. The constants
used in that markup are guides that are described in
further detail above. end note]
textDeflateTop (Top Deflate Text Shape) Specifies a text shape that shall match the normative
shape shown above.
©ISO/IEC 2016 – All rights reserved 3075\n\n--- Page 3086 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDeflateTop element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textDoubleWave1 (Double Wave 1 Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textDoubleWave1 element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textFadeDown (Downward Fade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textFadeDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textFadeLeft (Left Fade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textFadeLeft element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
3076 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3087 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
textFadeRight (Right Fade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textFadeRight element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textFadeUp (Upward Fade Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textFadeUp element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textInflate (Inflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textInflate element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textInflateBottom (Bottom Inflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
©ISO/IEC 2016 – All rights reserved 3077\n\n--- Page 3088 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
textInflateBottom element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textInflateTop (Top Inflate Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textInflateTop element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textNoShape (No Text Shape) Specifies that the text has no associated shape with it
and thus the text should not be warped but instead be
constrained by the normal text bounding box.
textPlain (Plain Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textPlain element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textRingInside (Inside Ring Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textRingInside element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
3078 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3089 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
textRingOutside (Outside Ring Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textRingOutside element in the preset text warp
electronic addenda of Annex D.
The constants used in that markup are guides that are
described in further detail above. end note]
textSlantDown (Downward Slant Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textSlantDown element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textSlantUp (Upward Slant Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textSlantUp element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textStop (Stop Sign Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
©ISO/IEC 2016 – All rights reserved 3079\n\n--- Page 3090 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
be used to achieve this effect is contained in the
textStop element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textTriangle (Triangle Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textTriangle element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textTriangleInverted (Inverted Triangle Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textTriangleInverted element in the preset text warp
electronic addenda of Annex D. The constants used in
that markup are guides that are described in further
detail above. end note]
textWave1 (Wave 1 Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textWave1 element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textWave2 (Wave 2 Text Shape)
3080 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3091 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textWave2 element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
textWave4 (Wave 4 Text Shape)
Specifies a text shape that shall match the normative
shape shown above.
[Note: An example of DrawingML markup which can
be used to achieve this effect is contained in the
textWave4 element in the preset text warp electronic
addenda of Annex D. The constants used in that
markup are guides that are described in further detail
above. end note]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextShapeType) is located in
§A.4.1. end note]
20.1.10.77 ST_TextSpacingPercentOrPercentString (Text Spacing Percent)
This simple type specifies that its contents will contain a text font spacing percentage. See the union's member
types for details.
This simple type is a union of the following types:
 The ST_Percentage simple type (§22.9.2.9).
[Note: The W3C XML Schema definition of this simple type’s content model
(ST_TextSpacingPercentOrPercentString) is located in §A.4.1. end note]
20.1.10.78 ST_TextSpacingPoint (Text Spacing Point)
This simple type specifies the Text Spacing that is used in terms of font point size.
This simple type's contents are a restriction of the W3C XML Schema int datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 0.
©ISO/IEC 2016 – All rights reserved 3081\n\n--- Page 3092 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 This simple type has a maximum value of less than or equal to 158400.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextSpacingPoint) is located in
§A.4.1. end note]
20.1.10.79 ST_TextStrikeType (Text Strike Type)
This simple type specifies the strike type.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
dblStrike (Text Strike Enum ( Double Strike )) A double strikethrough applied on the text
noStrike (Text Strike Enum ( No Strike )) No strike is applied to the text
sngStrike (Text Strike Enum ( Single Strike )) A single strikethrough is applied to the text
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextStrikeType) is located in
§A.4.1. end note]
20.1.10.80 ST_TextTabAlignType (Text Tab Alignment Types)
This simple type specifies the text tab alignment types.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
ctr (Text Tab Alignment Enum ( Center )) The text at this tab stop is center aligned.
dec (Text Tab Alignment Enum ( Decimal )) At this tab stop, the decimals are lined up. From a
user's point of view, the text here behaves as right
aligned until the decimal, and then as left aligned after
the decimal.
l (Text Tab Alignment Enum ( Left)) The text at this tab stop is left aligned.
r (Text Tab Alignment Enum ( Right )) The text at this tab stop is right aligned.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextTabAlignType) is located in
§A.4.1. end note]
20.1.10.81 ST_TextTypeface (Text Typeface)
This simple type specifies the way we represent a font typeface.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
3082 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3093 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextTypeface) is located in
§A.4.1. end note]
20.1.10.82 ST_TextUnderlineType (Text Underline Types)
This simple type specifies the text underline types that is used.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
dash (Text Underline Enum ( Dashed )) Underline the text with a single, dashed line of normal
thickness.
dashHeavy (Text Underline Enum ( Heavy Dashed )) Underline the text with a single, dashed, thick line.
dashLong (Text Underline Enum ( Long Dashed )) Underline the text with a single line consisting of long
dashes of normal thickness.
dashLongHeavy (Text Underline Enum ( Heavy Long Underline the text with a single line consisting of long,
Dashed )) thick dashes.
dbl (Text Underline Enum ( Double )) Underline the text with two lines of normal thickness.
dotDash (Text Underline Enum ( Dot Dash )) Underline the text with a single line of normal
thickness consisting of repeating dots and dashes.
dotDashHeavy (Text Underline Enum ( Heavy Dot Underline the text with a single, thick line consisting of
Dash )) repeating dots and dashes.
dotDotDash (Text Underline Enum ( Dot Dot Dash )) Underline the text with a single line of normal
thickness consisting of repeating two dots and dashes.
dotDotDashHeavy (Text Underline Enum ( Heavy Dot Underline the text with a single, thick line consisting of
Dot Dash )) repeating two dots and dashes.
dotted (Text Underline Enum ( Dotted )) Underline the text with a single, dotted line of normal
thickness.
dottedHeavy (Text Underline Enum ( Heavy Dotted )) Underline the text with a single, thick, dotted line.
heavy (Text Underline Enum ( Heavy )) Underline the text with a single, thick line.
none (Text Underline Enum ( None )) The reason we cannot implicitly have noUnderline be
the scenario where underline is not specified is
because not being specified implies deriving from a
particular style and the user might want to override
that and make some text not be underlined even
though the style says otherwise.
sng (Text Underline Enum ( Single )) Underline the text with a single line of normal
thickness.
wavy (Text Underline Enum ( Wavy )) Underline the text with a single wavy line of normal
thickness.
wavyDbl (Text Underline Enum ( Double Wavy )) Underline the text with two wavy lines of normal
©ISO/IEC 2016 – All rights reserved 3083\n\n--- Page 3094 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
thickness.
wavyHeavy (Text Underline Enum ( Heavy Wavy )) Underline the text with a single, thick wavy line.
words (Text Underline Enum ( Words )) Underline just the words and not the spaces between
them.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextUnderlineType) is located in
§A.4.1. end note]
20.1.10.83 ST_TextVerticalType (Vertical Text Types)
If there is vertical text, determines what kind of vertical text is going to be used.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
eaVert (Vertical Text Type Enum ( East Asian Vertical )) A special version of vertical text, where some fonts are
displayed as if rotated by 90 degrees while some fonts
(mostly East Asian) are displayed vertical.
horz (Vertical Text Type Enum ( Horizontal )) Horizontal text. This should be default.
mongolianVert (Vertical Text Type Enum ( Mongolian A special version of vertical text, where some fonts are
Vertical )) displayed as if rotated by 90 degrees while some fonts
(mostly East Asian) are displayed vertical. The
difference between this and the eastAsianVertical is
the text flows top down then LEFT RIGHT, instead of
RIGHT LEFT
vert (Vertical Text Type Enum ( Vertical )) Determines if all of the text is vertical orientation
(each line is 90 degrees rotated clockwise, so it goes
from top to bottom; each next line is to the left from
the previous one).
vert270 (Vertical Text Type Enum ( Vertical 270 )) Determines if all of the text is vertical orientation
(each line is 270 degrees rotated clockwise, so it goes
from bottom to top; each next line is to the right from
the previous one).
wordArtVert (Vertical Text Type Enum ( WordArt Determines if all of the text is vertical ("one letter on
Vertical )) top of another").
wordArtVertRtl (Vertical WordArt Right to Left) Specifies that vertical WordArt should be shown from
right to left rather than left to right.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextVerticalType) is located in
§A.4.1. end note]
3084 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3095 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.1.10.84 ST_TextVertOverflowType (Text Vertical Overflow)
This simple type specifies the text vertical overflow.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
clip (Text Overflow Enum ( Clip )) Pay attention to top and bottom barriers. Provide no
indication that there is text which is not visible.
ellipsis (Text Overflow Enum ( Ellipsis )) Pay attention to top and bottom barriers. Use an
ellipsis to denote that there is text which is not visible.
overflow (Text Overflow Enum ( Overflow )) Overflow the text and pay no attention to top and
bottom barriers.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextVertOverflowType) is
located in §A.4.1. end note]
20.1.10.85 ST_TextWrappingType (Text Wrapping Types)
Text Wrapping Types
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
none (Text Wrapping Type Enum ( None )) No wrapping occurs on this text body. Words spill out
without paying attention to the bounding rectangle
boundaries.
square (Text Wrapping Type Enum ( Square )) Determines whether we wrap words within the
bounding rectangle.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextWrappingType) is located in
§A.4.1. end note]
20.1.10.86 ST_TileFlipMode (Tile Flip Mode)
This simple type indicates whether/how to flip the contents of a tile region when using it to fill a larger fill
region.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 3085\n\n--- Page 3096 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
none (None)
Tiles are not flipped.
x (Horizontal)
Tiles are flipped horizontally.
xy (Horizontal and Vertical)
Tiles are flipped both horizontally and vertically.
3086 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3097 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
y (Vertical)
Tiles are flipped vertically.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TileFlipMode) is located in
§A.4.1. end note]
20.1.10.87 ST_TextBulletSize (Bullet Size Percentage)
This simple type specifies the range that the bullet percent can be. A bullet percent is the size of the bullet with
respect to the text that should follow it, with a minimum size of 25% and maximum size of 400%.
This simple type is a union of the following types:
 The ST_TextBulletSizePercent simple type (§20.1.10.62)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextBulletSize) is located in §
A.4.1. end note]
20.2 DrawingML - Picture
These elements encompass the definition of pictures within the DrawingML framework. While pictures are in
many ways very similar to shapes they have specific properties that are unique in order to optimize for picture-
specific scenarios. Some of these properties include Fill behavior, Border behavior and Resize behavior.
©ISO/IEC 2016 – All rights reserved 3087\n\n--- Page 3098 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.2.1 Table of Contents
This subclause is informative.
20.2.2 Elements .................................................................................................................................... 3088
20.2.2.1 blipFill (Picture Fill) ...................................................................................................................... 3088
20.2.2.2 cNvPicPr (Non-Visual Picture Drawing Properties) ..................................................................... 3091
20.2.2.3 cNvPr (Non-Visual Drawing Properties) ...................................................................................... 3091
20.2.2.4 nvPicPr (Non-Visual Picture Properties) ...................................................................................... 3094
20.2.2.5 pic (Picture) .................................................................................................................................. 3094
20.2.2.6 spPr (Shape Properties) ............................................................................................................... 3095
End of informative text.
20.2.2 Elements
The following section defines the Picture portion of the DrawingML framework.
20.2.2.1 blipFill (Picture Fill)
This element specifies the type of picture fill that the picture object has. Because a picture has a picture fill
already by default, it is possible to have two fills specified for a picture object. An example of this is shown
below.
[Example: Consider the picture below that has a blip fill applied to it. The image used to fill this picture object
has transparent pixels instead of white pixels.
<pic:pic>
…
<pic:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</pic:blipFill>
…
</pic:pic>
3088 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3099 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The above picture object is shown as an example of this fill type. end example]
[Example: Consider now the same picture object but with an additional gradient fill applied within the shape
properties portion of the picture.
<pic:pic>
…
<pic:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</pic:blipFill>
<pic:spPr>
<a:gradFill>
<a:gsLst>
<a:gs pos="0">
<a:schemeClr val="tx2">
<a:shade val="50000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="39999">
<a:schemeClr val="tx2">
<a:tint val="20000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="70000">
<a:srgbClr val="C4D6EB"/>
</a:gs>
<a:gs pos="100000">
<a:schemeClr val="bg1"/>
©ISO/IEC 2016 – All rights reserved 3089\n\n--- Page 3100 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</a:gs>
</a:gsLst>
</a:gradFill>
</pic:spPr>
…
</pic:pic>
The above picture object is shown as an example of this double fill type. end example]
Attributes Description
dpi (DPI Setting) Specifies the DPI (dots per inch) used to calculate the size of the blip. If not present or
zero, the DPI in the blip is used.
Namespace:
http://purl.oclc.or [Note: This attribute is primarily used to keep track of the picture quality within a
g/ooxml/drawing document. There are different levels of quality needed for print than on-screen viewing
ml/main and thus a need to track this information. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
rotWithShape Specifies that the fill should rotate with the shape. That is, when the shape that has been
(Rotate With Shape) filled with a picture and the containing shape (say a rectangle) is transformed with a
rotation then the fill is transformed with the same rotation.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the W3C XML Schema boolean
g/ooxml/drawing datatype.
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_BlipFillProperties) is located in
§A.4.1. end note]
3090 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3101 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.2.2.2 cNvPicPr (Non-Visual Picture Drawing Properties)
This element specifies the non-visual properties for the picture canvas. These properties are to be used by the
generating application to determine how certain properties are to be changed for the picture object in question.
[Example: Consider the following DrawingML.
<pic:pic>
…
<pic:nvPicPr>
<pic:cNvPr id="4" name="Lilly.jpg"/>
<pic:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</p:cNvPicPr>
<pic:nvPr/>
</pic:nvPicPr>
…
</pic:pic>
end example]
Attributes Description
preferRelativeResi Specifies if the user interface should show the resizing of the picture based on the
ze (Relative Resize picture's current size or its original size. If this attribute is set to true, then scaling is
Preferred) relative to the original picture size as opposed to the current picture size.
Namespace: [Example: Consider the case where a picture has been resized within a document and is
http://purl.oclc.or now 50% of the originally inserted picture size. Now if the user chooses to make a later
g/ooxml/drawing adjustment to the size of this picture within the generating application, then the value of
ml/main this attribute should be checked.
If this attribute is set to true then a value of 50% is shown. Similarly, if this attribute is set
to false, then a value of 100% should be shown because the picture has not yet been
resized from its current (smaller) size. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualPictureProperties) is
located in §A.4.1. end note]
20.2.2.3 cNvPr (Non-Visual Drawing Properties)
This element specifies non-visual canvas properties. This allows for additional information that does not affect
the appearance of the picture to be stored.
©ISO/IEC 2016 – All rights reserved 3091\n\n--- Page 3102 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following DrawingML.
<pic:pic>
…
<pic:nvPicPr>
<p:cNvPr id="4" name="Lilly.jpg"/>
</pic:nvPicPr>
…
</pic:pic>
end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications which do not display the current object.
Namespace: If this element is omitted, then no alternative text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text which can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
Namespace: This attribute determines whether the object is rendered or made hidden. [Note: An
http://purl.oclc.or application can have settings which allow this object to be viewed. end note]
g/ooxml/drawing
ml/main If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
[Example: Consider an inline DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
3092 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3103 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
Namespace:
http://purl.oclc.or If multiple objects within the same document share the same id attribute value, then the
g/ooxml/drawing document shall be considered non-conformant.
ml/main
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object defined as follows:
g/ooxml/drawing
ml/main < … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
Namespace: If this attribute is omitted, then no title text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
©ISO/IEC 2016 – All rights reserved 3093\n\n--- Page 3104 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.2.2.4 nvPicPr (Non-Visual Picture Properties)
This element specifies the non visual properties for a picture. This allows for additional information that does
not affect the appearance of the picture to be stored.
[Example: Consider the following DrawingML.
<pic:pic>
…
<pic:nvPicPr>
…
</pic:nvPicPr>
…
</pic:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_PictureNonVisual) is located in
§A.4.2. end note]
20.2.2.5 pic (Picture)
This element specifies the existence of a picture object within the document.
[Example: Consider the following DrawingML that specifies the existence of a picture within a document. This
picture can have non-visual properties, a picture fill as well as shape properties attached to it.
<pic:pic>
<pic:nvPicPr>
<pic:cNvPr id="4" name="lake.JPG" descr="Picture of a Lake" />
<pic:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</pic:cNvPicPr>
<pic:nvPr/>
</pic:nvPicPr>
<pic:blipFill>
…
</pic:blipFill>
<pic:spPr>
…
</pic:spPr>
</pic:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Picture) is located in §A.4.2. end
note]
3094 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3105 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.2.2.6 spPr (Shape Properties)
This element specifies the visual shape properties that can be applied to a picture. These are the same
properties that are allowed to describe the visual properties of a shape but are used here to describe the visual
appearance of a picture within a document. This allows for a picture to have both the properties of a shape as
well as picture specific properties that are allowed under the pic element.
Attributes Description
bwMode (Black and Specifies that the picture should be rendered using only black and white coloring. That is
White Mode) the coloring information for the picture should be converted to either black or white
when rendering the picture.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main [Note: This does not mean that the picture itself that is stored within the file is
necessarily a black and white picture. This attribute instead sets the rendering mode that
the picture has applied to when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeProperties) is located in
§A.4.1. end note]
20.3 DrawingML - Locked Canvas
Within a DrawingML object, a locked canvas allows DrawingML objects to be placed in a format where they can
be viewed but not edited by the hosting application. This allows DrawingML objects not supported by an
application to be included and viewed in applications where they cannot be edited.
20.3.1 Table of Contents
This subclause is informative.
20.3.2 Basics ......................................................................................................................................... 3095
20.3.2.1 lockedCanvas (Locked Canvas Container) ................................................................................... 3095
End of informative text.
20.3.2 Basics
This section specifies a locked canvas within the basic DrawingML framework.
20.3.2.1 lockedCanvas (Locked Canvas Container)
The locked canvas element acts as a container for more advanced drawing objects. The notion of a locked
canvas comes from the fact that the generating application opening the file cannot create this object and can
©ISO/IEC 2016 – All rights reserved 3095\n\n--- Page 3106 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
thus not perform edits either. Thus the drawing object is locked from all UI adjustments that would normally
take place.
[Note: The W3C XML Schema definition of this element’s content model (CT_GvmlGroupShape) is located in
§A.4.1. end note]
20.4 DrawingML - WordprocessingML Drawing
Within a WordprocessingML document, it is possible to include graphical DrawingML objects:
 Pictures (§20.2)
 Locked Canvases (§20.3)
 Diagrams (§21.4)
 Charts (§21.2)
When these objects are present in a word processing document, it is necessary to include information which
specifies how the objects shall be positioned relative to the paginated document. [Example: Whether the object
is displayed in line with text. end example]
The WordprocessingML Drawing namespace acts in this capacity, specifying all information necessary to anchor
and display DrawingML objects within a word processing document.
[Example: Consider a DrawingML picture which must be displayed in the center of the printed page on which it
appears, modifying the flow of text as necessary. This object would be specified as follows:
<w:r>
<w:drawing>
<wp:anchor relativeHeight="10" allowOverlap="true">
<wp:positionH relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionH>
<wp:positionV relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionV>
<wp:extent cx="2441542" cy="1828800"/>
<wp:wrapSquare wrapText="bothSides"/>
<a:graphic>
…
</a:graphic>
</wp:anchor>
</w:drawing>
</w:r>
3096 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3107 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The anchor element (§20.4.2.3) specifies that this object is not positioned in line with text, and its child
elements specify that the object is centered on the page horizontally and vertically (§20.4.2.10; §20.4.2.11), and
that text can wrap around it in a square (§20.4.2.17). end example]
20.4.1 Table of Contents
This subclause is informative.
20.4.2 Elements .................................................................................................................................... 3098
20.4.2.1 align (Relative Horizontal Alignment) .......................................................................................... 3098
20.4.2.2 align (Relative Vertical Alignment) .............................................................................................. 3099
20.4.2.3 anchor (Anchor for Floating DrawingML Object) ........................................................................ 3099
20.4.2.4 cNvGraphicFramePr (Common DrawingML Non-Visual Properties) ........................................... 3106
20.4.2.5 docPr (Drawing Object Non-Visual Properties) ........................................................................... 3107
20.4.2.6 effectExtent (Object Extents Including Effects) ........................................................................... 3109
20.4.2.7 extent (Drawing Object Size) ....................................................................................................... 3112
20.4.2.8 inline (Inline DrawingML Object) ................................................................................................. 3113
20.4.2.9 lineTo (Wrapping Polygon Line End Position) ............................................................................. 3116
20.4.2.10 positionH (Horizontal Positioning) .............................................................................................. 3118
20.4.2.11 positionV (Vertical Positioning) ................................................................................................... 3119
20.4.2.12 posOffset (Absolute Position Offset) ........................................................................................... 3120
20.4.2.13 simplePos (Simple Positioning Coordinates) ............................................................................... 3120
20.4.2.14 start (Wrapping Polygon Start) .................................................................................................... 3121
20.4.2.15 wrapNone (No Text Wrapping) ................................................................................................... 3122
20.4.2.16 wrapPolygon (Wrapping Polygon) ............................................................................................... 3123
20.4.2.17 wrapSquare (Square Wrapping) .................................................................................................. 3124
20.4.2.18 wrapThrough (Through Wrapping) ............................................................................................. 3127
20.4.2.19 wrapTight (Tight Wrapping) ........................................................................................................ 3130
20.4.2.20 wrapTopAndBottom (Top and Bottom Wrapping)...................................................................... 3133
20.4.2.21 bg (Background Formatting) ........................................................................................................ 3134
20.4.2.22 bodyPr (Body Properties) ............................................................................................................ 3134
20.4.2.23 cNvCnPr (Non-Visual Connector Shape Drawing Properties) ...................................................... 3137
20.4.2.24 cNvContentPartPr (Non-Visual Content Part Drawing Properties) ............................................. 3137
20.4.2.25 cNvFrPr (Non-Visual Graphic Frame Drawing Properties)........................................................... 3138
20.4.2.26 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties) ....................................................... 3138
20.4.2.27 cNvPr (Non-Visual Drawing Properties) ...................................................................................... 3138
20.4.2.28 cNvSpPr (Non-Visual Drawing Properties for a Shape) ............................................................... 3140
20.4.2.29 contentPart (Content Part) .......................................................................................................... 3140
20.4.2.30 extLst (Extension List) .................................................................................................................. 3142
20.4.2.31 graphicFrame (Graphical object container) ................................................................................. 3142
20.4.2.32 grpSp (Group Shape) ................................................................................................................... 3142
20.4.2.33 grpSpPr (Group Shape Properties) .............................................................................................. 3142
20.4.2.34 linkedTxbx (Textual contents of shape) ....................................................................................... 3143
20.4.2.35 spPr (Shape Properties) ............................................................................................................... 3143
20.4.2.36 style (Shape Style) ....................................................................................................................... 3143
20.4.2.37 txbx (Textual contents of shape) ................................................................................................. 3144
20.4.2.38 txbxContent (Rich Text Box Content Container) ......................................................................... 3144
20.4.2.39 wgp (WordprocessingML Shape Group)...................................................................................... 3144
©ISO/IEC 2016 – All rights reserved 3097\n\n--- Page 3108 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.40 whole (Whole E2O Formatting) ................................................................................................... 3144
20.4.2.41 wpc (WordprocessingML Drawing Canvas) ................................................................................. 3144
20.4.2.42 wsp (WordprocessingML Shape) ................................................................................................. 3145
20.4.2.43 xfrm (2D Transform for Graphic Frames) .................................................................................... 3145
20.4.3 Simple Types .............................................................................................................................. 3146
20.4.3.1 ST_AlignH (Relative Horizontal Alignment Positions).................................................................. 3146
20.4.3.2 ST_AlignV (Vertical Alignment Definition) ................................................................................... 3147
20.4.3.3 ST_PositionOffset (Absolute Position Offset Value) .................................................................... 3148
20.4.3.4 ST_RelFromH (Horizontal Relative Positioning) .......................................................................... 3149
20.4.3.5 ST_RelFromV (Vertical Relative Positioning) ............................................................................... 3150
20.4.3.6 ST_WrapDistance (Distance from Text) ...................................................................................... 3151
20.4.3.7 ST_WrapText (Text Wrapping Location)...................................................................................... 3151
End of informative text.
20.4.2 Elements
The following elements define the contents of the WordprocessingML Drawing namespace:
20.4.2.1 align (Relative Horizontal Alignment)
This element specifies how a DrawingML object shall be horizontally aligned relative to the horizontal alignment
base defined by the parent element. Once an alignment base is defined, this element shall determine how the
DrawingML object shall be aligned relative to that location.
[Example: Consider a picture in a WordprocessingML document which has been aligned relative to the edge of
the page - the left of the page horizontally, and the top of the page vertically. This alignment would be specified
as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:align>left</wp:align>
</wp:positionH>
…
</wp:anchor>
The align element with a value of left specifies that for the horizontal positioning defined by the parent
element (in this case, positioning relative to the page), the picture must be aligned to the left edge of the page.
end example]
The possible values for this element are defined by the ST_AlignH simple type (§20.4.3.1).
[Note: The W3C XML Schema definition of this element’s content model (ST_AlignH) is located in §A.4.4. end
note]
3098 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3109 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.2 align (Relative Vertical Alignment)
This element specifies how a DrawingML object shall be vertically aligned relative to the vertical alignment base
defined by the parent element. Once an alignment base is defined, this element shall determine how the
DrawingML object shall be aligned relative to that location.
[Example: Consider a picture in a WordprocessingML document which has been aligned relative to the edge of
the page - the left of the page horizontally, and the top of the page vertically. This alignment would be specified
as follows:
<wp:anchor … >
<wp:positionV relativeFrom="page">
<wp:align>top</wp:align>
</wp:positionH>
…
</wp:anchor>
The align element with a value of top specifies that for the vertical positioning defined by the parent element
(in this case, positioning relative to the page), the picture must be aligned to the top edge of the page. end
example]
The possible values for this element are defined by the ST_AlignV simple type (§20.4.3.2).
[Note: The W3C XML Schema definition of this element’s content model (ST_AlignV) is located in §A.4.4. end
note]
20.4.2.3 anchor (Anchor for Floating DrawingML Object)
This element specifies that the DrawingML object located at this position in the document is a floating object.
Within a WordprocessingML document, drawing objects can exist in two states:
 Inline - The drawing object is in line with the text, and affects the line height and layout of its line (like a
character glyph of similar size).
 Floating - The drawing object is anchored within the text, but can be absolutely positioned in the
document relative to the page.
When this element encapsulates the DrawingML object's information, then all child elements shall dictate the
positioning of this object as a floating object on the page.
[Example: Consider a WordprocessingML document where the anchor for a floating DrawingML object must be
the first piece of run content within a paragraph. That paragraph's content would be specified as follows:
©ISO/IEC 2016 – All rights reserved 3099\n\n--- Page 3110 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<w:p>
<w:r>
<w:drawing>
<wp:anchor … >
…
</wp:anchor>
</w:drawing>
</w:r>
</w:p>
The anchor element, when present as the child element of the drawing element, specifies that this DrawingML
object must be positioned as a floating object based on the values of its child elements. end example]
Attributes Description
allowOverlap Specifies whether a DrawingML object which intersects another DrawingML object at
(Allow Objects to display time is allowed to overlap the contents of the other DrawingML object. If a
Overlap) DrawingML object cannot overlap other DrawingML object, it shall be repositioned when
displayed to prevent this overlap as needed.
[Example: Consider a document with two DrawingML objects which are allowed to
overlap each other. This would be specified as follows within each object's anchor
markup:
<wp:anchor allowOverlap="true" … >
…
</wp:anchor>
The allowOverlap attribute has a value of true, which specifies that this object must be
allowed to overlap other objects when it is displayed on the document. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
behindDoc (Display Specifies whether this floating DrawingML object is displayed behind the text of the
Behind Document document when the document is displayed. When a DrawingML object is displayed
Text) within a WordprocessingML document, that object can intersect with text in the
document. This attribute shall determine whether the text or the object is rendered on
top in case of overlapping.
[Example: Consider a floating DrawingML object which must be displayed above any text
which it intersects within the document's content. This setting would be specified as
follows:
<wp:anchor behindDoc="false" … >
…
</wp:anchor>
3100 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3111 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The behindDoc attribute has a value of false, which specifies that the DrawingML
object is displayed above the text of the document in z-order. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
distB (Distance Specifies the minimum distance which shall be maintained between the bottom edge of
From Text on this drawing object and any subsequent text within the document when this graphical
Bottom Edge) object is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its bottom edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distB="457200" … >
…
</wp:anchor>
The distB attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distL (Distance Specifies the minimum distance which shall be maintained between the left edge of this
From Text on Left drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-quarter of an inch
of padding between its left edge and the nearest text. This setting would be specified as
follows:
©ISO/IEC 2016 – All rights reserved 3101\n\n--- Page 3112 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<wp:anchor distL="228600" … >
…
</wp:anchor>
The distL attribute specifies that the padding distance must be 228600 EMUs or one-
quarter of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distR (Distance Specifies the minimum distance which shall be maintained between the right edge of this
From Text on Right drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-quarter of an inch
of padding between its right edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distR="228600" … >
…
</wp:anchor>
The distR attribute specifies that the padding distance must be 228600 EMUs or one-
quarter of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distT (Distance Specifies the minimum distance which shall be maintained between the top edge of this
From Text on Top drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
3102 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3113 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its top edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distT="457200" … >
…
</wp:anchor>
The distT attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
hidden (Hidden) Specifies whether this floating DrawingML object is displayed. When a DrawingML object
is displayed within a WordprocessingML document, that object can be hidden (i.e.
present, but not visible). This attribute shall determine whether the object is rendered or
made hidden. [Note: An application can have settings which allow this object to be
viewed. end note]
If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e. not
hidden).
[Example: Consider a floating DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<wp:anchor hidden="true" … >
…
</wp:anchor>
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
layoutInCell Specifies how this DrawingML object behaves when its anchor is located in a table cell;
(Layout In Table and its specified position would cause it to intersect with a table cell displayed in the
Cell) document. That behavior shall be as follows:
 When this attribute has a value of true, then the object shall be positioned
within the existing table cell, causing the cell to be resized as needed. This means
that all positioning shall be relative to the cell and not the line on which the table
appears.
 When this attribute has a value of false, then the object shall be positioned as
specified, but the table shall be resized and/or relocated within the document as
needed to accommodate the object. This means that all positioning shall be
©ISO/IEC 2016 – All rights reserved 3103\n\n--- Page 3114 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
relative to the line on which the table appears and not the cell in which the
anchor is present.
[Example: Consider a DrawingML picture which must be displayed in the center of the
document. If the object is contained within a table and is defined as follows:
<wp:anchor layoutInCell="true" … >
…
</wp:anchor>
The layoutInCell attribute has a value of true, which specifies that the object can be
placed within the cell if needed, for example:
If the layoutInCell attribute was now set to false, the object must be laid out outside of
the cell, causing the table to be repositioned:
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
locked (Lock Specifies that the anchor location for this object shall not be modified at runtime when
3104 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3115 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Anchor) an application edits the contents of this document. [Guidance: An application might have
automatic behaviors which reposition the anchor for a DrawingML object based on user
interaction - for example, moving it from one page to another as needed. This element
must tell applications not to perform any such behaviors. end guidance]
[Example: Consider a floating DrawingML object which must have its anchor locked at the
current location. This setting would be specified as follows:
<wp:anchor locked="true" … >
…
</wp:anchor>
The locked attribute has a value of true, which specifies that the DrawingML object's
current anchor location must not be changed by applications editing this content. end
example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
relativeHeight Specifies the relative Z-ordering of all DrawingML objects in this document. Each floating
(Relative Z-Ordering DrawingML object shall have a Z-ordering value, which determines which object is
Position) displayed when any two objects intersect. Higher values shall indicate higher Z-order;
lower values shall indicate lower Z-order.
This attribute shall only indicate the Z-order with respect to other objects in the
document which have an identical behindDoc attribute value. All objects with a
behindDoc value of false shall be displayed above elements with a value of true.
[Example: Consider two floating DrawingML objects as follows:
<wp:anchor relativeHeight="5" … >
…
</wp:anchor>
…
<wp:anchor relativeHeight="8" … >
…
</wp:anchor>
The relativeHeight attribute of the second object is 8, which specifies that the second
DrawingML object must be at a higher Z-order than the first and must be displayed
whenever the two overlap. end example]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
simplePos (Page Specifies that this object shall be positioned using the positioning information in the
©ISO/IEC 2016 – All rights reserved 3105\n\n--- Page 3116 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Positioning) simplePos child element (§20.4.2.13). This positioning, when specified, positions the
object on the page by placing its top left point at the x-y coordinates specified by that
element.
If this element is omitted, then this object shall not use the simple positioning
information in the simplePos element, even when present.
[Example: Consider a floating DrawingML object which must be positioned at the top left
corner of the page using simple positioning. This setting would be specified as follows:
<wp:anchor simplePos="true" … >
<wp:simplePos x="0" y="0" />
…
</wp:anchor>
The simplePos attribute has a value of true, which specifies that the DrawingML object's
current position must be dictated by the simplePos element, and hence placed at 0,0.
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Anchor) is located in §A.4.4. end
note]
20.4.2.4 cNvGraphicFramePr (Common DrawingML Non-Visual Properties)
This element specifies common non-visual DrawingML object properties for the parent DrawingML object. These
properties are specified as child elements of this element.
[Example: Consider a DrawingML object in a WordprocessingML document defined as follows:
<wp:inline>
…
<wp:cNvGraphicFramePr>
<a:graphicFrameLocks … />
</wp:cNvGraphicFramePr>
</wp:inline>
The cNvGraphicFramePr element contains a set of common non-visual properties as defined by DrawingML.
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualGraphicFrameProperties)
is located in §A.4.1. end note]
3106 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3117 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.5 docPr (Drawing Object Non-Visual Properties)
This element specifies non-visual object properties for the parent DrawingML object. These properties are
specified as child elements of this element.
[Example: Consider a DrawingML object in a WordprocessingML document defined as follows:
<wp:inline>
…
<wp:docPr id="1" name="Example Object">
<a:hlinkClick … />
<a:hlinkHover … />
</wp:docPr>
</wp:inline>
The docPr element contains a set of common non-visual properties for this object. end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications which do not display the current object.
Namespace: If this element is omitted, then no alternative text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text which can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
Namespace: This attribute determines whether the object is rendered or made hidden. [Note: An
http://purl.oclc.or application can have settings which allow this object to be viewed. end note]
g/ooxml/drawing
ml/main If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
[Example: Consider an inline DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
©ISO/IEC 2016 – All rights reserved 3107\n\n--- Page 3118 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
Namespace:
http://purl.oclc.or If multiple objects within the same document share the same id attribute value, then the
g/ooxml/drawing document shall be considered non-conformant.
ml/main
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object defined as follows:
g/ooxml/drawing
ml/main < … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
Namespace: If this attribute is omitted, then no title text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
3108 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3119 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
20.4.2.6 effectExtent (Object Extents Including Effects)
This element specifies the additional extent which shall be added to each edge of the image (top, bottom, left,
right) in order to compensate for any drawing effects applied to the DrawingML object.
The extent element (§20.4.2.7) specifies the size of the actual DrawingML object; however, an object can have
effects applied which change its overall size [Example: A reflection and/or shadow effect. end example]. The
additional size for each edge of the shape shall be stored on this element, and used to calculate the appropriate
wrapping for wrap types without a wrapping polygon and the appropriate line height for inline objects.
[Example: Consider the following DrawingML image:
This object has no effects, and hence would have the following effect extents:
<wp:effectExtents b="0" t="0" l="0" r="0" />
However, if a shadow effect was applied which added effects to the right of the image:
Then the additional extent the right side would be specified in the r attribute on this element:
<wp:effectExtents b="0" t="0" l="0" r="695325" />
©ISO/IEC 2016 – All rights reserved 3109\n\n--- Page 3120 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The r attribute has a value of 695325, specifying that that 695325 EMUs must be added to the right side of the
image. end example]
Attributes Description
b (Additional Extent Specifies the additional length, in EMUs, which shall be added to the bottom edge of the
on Bottom Edge) DrawingML object to determine its actual bottom edge including effects.
[Example: Consider the following DrawingML image:
This image has an effect on all four sides, resulting in the following markup:
<wp:effectExtent l="504825" t="447675" r="771525" b="809625" />
The b attribute value of 809625 specifies that 809625 additional EMUs must be added to
the bottom of the image to compensate for the effects on the image. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
l (Additional Extent Specifies the additional length, in EMUs, which shall be added to the bottom edge of the
on Left Edge) DrawingML object to determine its actual bottom edge including effects.
[Example: Consider the following DrawingML image:
3110 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3121 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
This image has an effect on all four sides, resulting in the following markup:
<wp:effectExtent l="504825" t="447675" r="771525" b="809625" />
The l attribute value of 504825 specifies that 504825 additional EMUs must be added to
the bottom of the image to compensate for the effects on the image. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
r (Additional Extent Specifies the additional length, in EMUs, which shall be added to the bottom edge of the
on Right Edge) DrawingML object to determine its actual bottom edge including effects.
[Example: Consider the following DrawingML image:
This image has an effect on all four sides, resulting in the following markup:
©ISO/IEC 2016 – All rights reserved 3111\n\n--- Page 3122 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<wp:effectExtent l="504825" t="447675" r="771525" b="809625" />
The r attribute value of 771525 specifies that 771525 additional EMUs must be added to
the bottom of the image to compensate for the effects on the image. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
t (Additional Extent Specifies the additional length, in EMUs, which shall be added to the bottom edge of the
on Top Edge) DrawingML object to determine its actual bottom edge including effects.
[Example: Consider the following DrawingML image:
This image has an effect on all four sides, resulting in the following markup:
<wp:effectExtent l="504825" t="447675" r="771525" b="809625" />
The t attribute value of 447675 specifies that 447675 additional EMUs must be added to
the bottom of the image to compensate for the effects on the image. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_EffectExtent) is located in §A.4.4.
end note]
20.4.2.7 extent (Drawing Object Size)
This element specifies the extents of the parent DrawingML object within the document (i.e. its final height and
width).
3112 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3123 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider a DrawingML picture which is present in a WordprocessingML document and has an equal
height and width. This object would be specified as follows:
<wp:anchor relativeHeight="10" allowOverlap="true">
…
<wp:extent cx="1828800" cy="1828800"/>
…
</wp:anchor>
The extent element specifies via its attributes that this object has a height and width of 1828800 EMUs (English
Metric Units). end example]
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main <… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main < … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
20.4.2.8 inline (Inline DrawingML Object)
This element specifies that the DrawingML object located at this position in the document is an inline object.
Within a WordprocessingML document, drawing objects can exist in two states:
©ISO/IEC 2016 – All rights reserved 3113\n\n--- Page 3124 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Inline - The drawing object is in line with the text, and affects the line height and layout of its line (like a
character glyph of similar size).
 Floating - The drawing object is anchored within the text, but can be absolutely positioned in the
document relative to the page.
When this element encapsulates the DrawingML object's information, then all child elements shall dictate the
positioning of this object in line with text.
[Example: Consider a WordprocessingML document where an inline DrawingML object must be the first piece of
run content within a paragraph. That paragraph's content would be specified as follows:
<w:p>
<w:r>
<w:drawing>
<wp:inline>
…
</wp:inline>
</w:drawing>
</w:r>
</w:p>
The inline element, when present as the child element of the drawing element, specifies that this DrawingML
object must be positioned in line with the text of this paragraph, modifying line heights, etc. as necessary. end
example]
Attributes Description
distB (Distance Specifies the minimum distance which shall be maintained between the bottom edge of
From Text on this drawing object and any subsequent text within the document when this graphical
Bottom Edge) object is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its bottom edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distB="457200" … >
…
</wp:anchor>
3114 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3125 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The distB attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distL (Distance Specifies the minimum distance which shall be maintained between the left edge of this
From Text on Left drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-quarter of an inch
of padding between its left edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distL="228600" … >
…
</wp:anchor>
The distL attribute specifies that the padding distance must be 228600 EMUs or one-
quarter of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distR (Distance Specifies the minimum distance which shall be maintained between the right edge of this
From Text on Right drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-quarter of an inch
of padding between its right edge and the nearest text. This setting would be specified as
follows:
©ISO/IEC 2016 – All rights reserved 3115\n\n--- Page 3126 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<wp:anchor distR="228600" … >
…
</wp:anchor>
The distR attribute specifies that the padding distance must be 228600 EMUs or one-
quarter of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distT (Distance Specifies the minimum distance which shall be maintained between the top edge of this
From Text on Top drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
If this object is an inline object (i.e. has a parent element of inline), then this value shall
not have any effect when displaying the object in line with text, but can be maintained
and used if the object is subsequently changed to floating. If the wrapping element
[Example: wrapThrough or wrapSquare end example] present as a child element also
has a distance from text, then this value shall be ignored.
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its top edge and the nearest text. This setting would be specified as
follows:
<wp:anchor distT="457200" … >
…
</wp:anchor>
The distT attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
[Note: The W3C XML Schema definition of this element’s content model (CT_Inline) is located in §A.4.4. end
note]
20.4.2.9 lineTo (Wrapping Polygon Line End Position)
This element specifies a single point on the wrapping polygon for a DrawingML object. This point shall be the
termination of the edge of the wrapping polygon started by the previous start or lineTo element in document
order, and shall be the origin of the next edge on the same polygon.
3116 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3127 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The attributes on this element shall dictate the position of the point relative to the upper-left corner of the
actual object.
[Example: Consider the following basic wrapping polygon for a DrawingML object:
<wp:wrapPolygon>
<wp:start x="0" y="0" />
<wp:lineTo x="0" y="100" />
<wp:lineTo x="100" y="100" />
<wp:lineTo x="100" y="0" />
<wp:lineTo x="0" y="0" />
</wp:wrapPolygon>
The lineTo element defines each point of the wrapping polygon (in this case, the four points of the wrapping
square). end example]
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 3117\n\n--- Page 3128 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.10 positionH (Horizontal Positioning)
This element specifies the horizontal positioning of a floating DrawingML object within a WordprocessingML
document. This positioning is specified in two parts:
 Positioning Base - The relativeFrom attribute on this element specifies the part of the document from
which the positioning shall be calculated.
 Positioning - The child element of this element (align or posOffset) specifies how the object is
positioned relative to that base.
[Example: Consider a DrawingML picture which must be displayed in the center of the printed page on which it
appears, modifying the flow of text as necessary. This object would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionH>
<wp:positionV relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionV>
</wp:anchor>
The positionH element specifies that the object is horizontally positioned relative to the margin via the
relativeFrom attribute; and that the alignment relative to the margin is centered via the align element. end
example]
Attributes Description
relativeFrom Specifies the base to which the relative horizontal positioning of this object shall be
(Horizontal Position calculated.
Relative Base)
[Example: Consider a DrawingML picture which must be displayed at the bottom center
of the page. This object would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:align>center</wp:align>
</wp:positionH>
…
</wp:anchor>
The relativeFrom attribute specifies that the object is horizontally positioned relative to
the page. end example]
The possible values for this attribute are defined by the ST_RelFromH simple type
(§20.4.3.4).
3118 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3129 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_PosH) is located in §A.4.4. end
note]
20.4.2.11 positionV (Vertical Positioning)
This element specifies the vertical positioning of a floating DrawingML object within a WordprocessingML
document. This positioning is specified in two parts:
 Positioning Base - The relativeFrom attribute on this element specifies the part of the document from
which the positioning shall be calculated.
 Positioning - The child element of this element (align or posOffset) specifies how the object is
positioned relative to that base.
[Example: Consider a DrawingML picture which must be displayed in the center of the printed page on which it
appears, modifying the flow of text as necessary. This object would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionH>
<wp:positionV relativeFrom="margin">
<wp:align>center</wp:align>
</wp:positionV>
</wp:anchor>
The positionV element specifies that the object is vertically positioned relative to the margin via the
relativeFrom attribute; and that the alignment relative to the margin is centered via the align element. end
example]
Attributes Description
relativeFrom Specifies the base to which the relative vertical positioning of this object shall be
(Vertical Position calculated.
Relative Base)
[Example: Consider a DrawingML picture which must be displayed at the bottom center
of the page margins. This object would be specified as follows:
<wp:anchor … >
…
<wp:positionV relativeFrom="margin">
<wp:align>bottom</wp:align>
</wp:positionV>
</wp:anchor>
The relativeFrom attribute specifies that the object is horizontally positioned relative to
the margin. end example]
©ISO/IEC 2016 – All rights reserved 3119\n\n--- Page 3130 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_RelFromV simple type
(§20.4.3.5).
[Note: The W3C XML Schema definition of this element’s content model (CT_PosV) is located in §A.4.4. end
note]
20.4.2.12 posOffset (Absolute Position Offset)
This element specifies an absolute measurement for the positioning of a floating DrawingML object within a
WordprocessingML document. This measurement shall be calculated relative to the top left edge of the
positioning base specified by the parent element's relativeFrom attribute.
[Example: Consider a DrawingML picture which must be displayed one inch from the top of the page, and one-
half of an inch from the left edge of the page. This object would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:posOffset>914400</wp:posOffset>
</wp:positionH>
<wp:positionV relativeFrom="page">
<wp:posOffset>457200</wp:posOffset>
</wp:positionV>
</wp:anchor>
The posOffset element specifies the absolute positioning of the object relative to the top-left edge of the page
in EMUs. end example]
The possible values for this element are defined by the ST_PositionOffset simple type (§20.4.3.3).
[Note: The W3C XML Schema definition of this element’s content model (ST_PositionOffset) is located in §A.4.4.
end note]
20.4.2.13 simplePos (Simple Positioning Coordinates)
This element specifies the coordinates at which a DrawingML object shall be positioned relative to the top-left
edge of its page, when the simplePos attribute is specified on the anchor element (§20.4.2.3).
[Example: Consider a floating DrawingML object which must be positioned at the top left corner of the page
using simple positioning. This setting would be specified as follows:
<wp:anchor simplePos="true" … >
<wp:simplePos x="0" y="0" />
…
</wp:anchor>
3120 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3131 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The simplePos attribute has a value of true, which specifies that the DrawingML object's current position must
be dictated by the simplePos element, and hence placed at 0,0. end example]
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
20.4.2.14 start (Wrapping Polygon Start)
This element specifies the starting point on the wrapping polygon for a DrawingML object. This point shall be the
start and termination of the wrapping polygon for the parent object.
The attributes on this element shall dictate the position of the point relative to the upper-left corner of the
actual object.
[Example: Consider the following basic wrapping polygon for a DrawingML object:
©ISO/IEC 2016 – All rights reserved 3121\n\n--- Page 3132 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<wp:wrapPolygon>
<wp:start x="0" y="0" />
<wp:lineTo x="0" y="100" />
<wp:lineTo x="100" y="100" />
<wp:lineTo x="100" y="0" />
<wp:lineTo x="0" y="0" />
</wp:wrapPolygon>
The start element defines the start and end of the wrapping polygon (in this case, the four points of the
wrapping square). end example]
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
20.4.2.15 wrapNone (No Text Wrapping)
This element specifies that the parent DrawingML object shall not cause any text wrapping within the contents
of the host WordprocessingML document based on its display location. In effect, this setting shall place the
object in one of two locations:
3122 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3133 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 If the behindDoc attribute on the parent element is true, then the object shall be positioned behind the
text as it is normally displayed.
 If the behindDoc attribute on the parent element is false, then the object shall be positioned in front
of the text as it is normally displayed.
[Example: Consider a DrawingML picture which must be displayed in front of any text on the page. This object
would be specified as follows:
<wp:anchor relativeHeight="10" behindDoc="false">
…
<wp:wrapNone/>
</wp:anchor>
The wrapNone element specifies that the DrawingML object must not cause any text wrapping, and since the
behindDoc attribute is false, the object must be displayed in front of the text of the document. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapNone) is located in §A.4.4.
end note]
20.4.2.16 wrapPolygon (Wrapping Polygon)
This element specifies the wrapping polygon which shall be used to determine the extents to which text can
wrap around the specified object in the document. This polygon shall be defined by the following:
 The start element defines the coordinates of the origin of the wrap polygon
 Two or more lineTo elements define the point of the wrap polygon
If the set of child elements does not result in a closed polygon (the last lineTo element does not return to the
position specified by the start element), then a single additional line shall be inferred as needed to close the
wrapping polygon.
[Example: Consider the following basic wrapping polygon for a DrawingML object:
<wp:wrapPolygon>
<wp:start x="0" y="0" />
<wp:lineTo x="0" y="100" />
<wp:lineTo x="100" y="100" />
<wp:lineTo x="100" y="0" />
<wp:lineTo x="0" y="0" />
</wp:wrapPolygon>
The wrapPolygon element defines the object's text wrapping polygon (in this case, the four points of a square).
end example]
Attributes Description
edited (Wrapping Specifies that the wrap points for the wrapping polygon have been edited, and the
©ISO/IEC 2016 – All rights reserved 3123\n\n--- Page 3134 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Points Modified) resulting extents shall be recalculated to compensate when the document is next
opened.
[Example: Consider the following basic wrapping polygon for a DrawingML object:
<wp:wrapPolygon edited="true">
<wp:start x="0" y="0" />
<wp:lineTo x="0" y="100" />
<wp:lineTo x="50" y="50" />
<wp:lineTo x="0" y="0" />
</wp:wrapPolygon>
The edited attribute specifies that these wrap points have been changed since the
document was last rendered. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapPath) is located in §A.4.4. end
note]
20.4.2.17 wrapSquare (Square Wrapping)
This element specifies that text shall wrap around a virtual rectangle bounding this object. The bounds of the
wrapping rectangle shall be dictated by the extents including the addition of the effectExtent element as a child
of this element (if present) or the effectExtent present on the parent element.
[Example: Consider a DrawingML object using square wrapping and defined as follows:
<wp:anchor … >
…
<wp:wrapSquare wrapText="bothSides" />
</wp:anchor>
The wrapSquare element specifies that text must wrap around both sides of a rectangle around this object
which includes its effect extents. end example]
Attributes Description
distB (Distance Specifies the minimum distance which shall be maintained between the bottom edge of
From Text on this drawing object and any subsequent text within the document when this graphical
Bottom Edge) object is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
3124 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3135 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
padding between its bottom edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapSquare distB="457200" … />
</wp:anchor>
The distB attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distL (Distance Specifies the minimum distance which shall be maintained between the left edge of this
From Text on Left drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its left edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapSquare distL="457200" … />
</wp:anchor>
The distL attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distR (Distance Specifies the minimum distance which shall be maintained between the right edge of this
From Text on Right drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its right edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapSquare distR="457200" … />
©ISO/IEC 2016 – All rights reserved 3125\n\n--- Page 3136 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
</wp:anchor>
The distR attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distT (Distance Specifies the minimum distance which shall be maintained between the top edge of this
From Text (Top)) drawing object and any subsequent text within the document when this graphical object
is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its top edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapSquare distT="457200" … />
</wp:anchor>
The distT attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
wrapText (Text Specifies how text shall wrap around the object's left and right sides.
Wrapping Location)
[Example: Consider a floating DrawingML object which must allow text to wrap around its
left side only. This setting would be specified as follows:
<wp:anchor … >
…
<wp:wrapSquare wrapText="left" … />
</wp:anchor>
The wrapText attribute value of left specifies that text must only wrap around the let
side of the object. end example]
The possible values for this attribute are defined by the ST_WrapText simple type
(§20.4.3.7).
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapSquare) is located in §A.4.4.
end note]
3126 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3137 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.18 wrapThrough (Through Wrapping)
This element specifies that text shall wrap around the wrapping polygon bounding this object as defined by the
child wrapPolygon element. When this element specifies a wrapping polygon, it shall allow text to wrap within
the object's maximum left and right extents.
[Example: Consider an object with the following wrap points:
If this object uses tight wrapping, then text cannot be placed within the maximum left and right extents of the
wrap polygon at any location:
However, with through wrapping:
©ISO/IEC 2016 – All rights reserved 3127\n\n--- Page 3138 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Example: Consider a DrawingML object using through wrapping and defined as follows:
<wp:anchor … >
…
<wp:wrapThrough wrapText="bothSides">
…
</wp:wrapThrough>
</wp:anchor>
The wrapThrough element specifies that text must wrap through this object as defined by its wrap polygon. end
example]
Attributes Description
distL (Distance Specifies the minimum distance which shall be maintained between the left edge of this
From Text on Left drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its left edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapThrough distL="457200" … />
</wp:anchor>
The distL attribute specifies that the padding distance must be 457200 EMUs or one-half
3128 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3139 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distR (Distance Specifies the minimum distance which shall be maintained between the right edge of this
From Text on Right drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its right edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapThrough distR="457200" … />
</wp:anchor>
The distR attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
wrapText (Text Specifies how text shall wrap around the object's left and right sides.
Wrapping Location)
[Example: Consider a floating DrawingML object which must allow text to wrap around its
left side only. This setting would be specified as follows:
<wp:anchor … >
…
<wp:wrapThrough wrapText="left" … />
</wp:anchor>
The wrapText attribute value of left specifies that text must only wrap around the let
side of the object. end example]
The possible values for this attribute are defined by the ST_WrapText simple type
(§20.4.3.7).
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapThrough) is located in §A.4.4.
end note]
©ISO/IEC 2016 – All rights reserved 3129\n\n--- Page 3140 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.19 wrapTight (Tight Wrapping)
This element specifies that text shall wrap around the wrapping polygon bounding this object as defined by the
child wrapPolygon element. When this element specifies a wrapping polygon, it shall not allow text to wrap
within the object's maximum left and right extents.
[Example: Consider an object with the following wrap points:
If this object uses tight wrapping, then text cannot be placed within the maximum left and right extents of the
wrap polygon at any location:
However, with through wrapping:
3130 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3141 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Example: Consider a DrawingML object using tight wrapping and defined as follows:
<wp:anchor … >
…
<wp:wrapTight wrapText="bothSides">
…
</wp:wrapTight>
</wp:anchor>
The wrapTight element specifies that text must wrap through this object as defined by its wrap polygon. end
example]
Attributes Description
distL (Distance Specifies the minimum distance which shall be maintained between the left edge of this
From Test on Left drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its left edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapTight distL="457200" … />
</wp:anchor>
The distL attribute specifies that the padding distance must be 457200 EMUs or one-half
©ISO/IEC 2016 – All rights reserved 3131\n\n--- Page 3142 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distR (Distance Specifies the minimum distance which shall be maintained between the right edge of this
From Text on Right drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its right edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapTight distR="457200" … />
</wp:anchor>
The distR attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
wrapText (Text Specifies how text shall wrap around the object's left and right sides.
Wrapping Location)
[Example: Consider a floating DrawingML object which must allow text to wrap around its
left side only. This setting would be specified as follows:
<wp:anchor … >
…
<wp:wrapTight wrapText="left" … />
</wp:anchor>
The wrapText attribute value of left specifies that text must only wrap around the let
side of the object. end example]
The possible values for this attribute are defined by the ST_WrapText simple type
(§20.4.3.7).
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapTight) is located in §A.4.4. end
note]
3132 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3143 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.20 wrapTopAndBottom (Top and Bottom Wrapping)
This element specifies that text shall wrap around the top and bottom of this object, but not its left or right
edges.
[Example: Consider a DrawingML object using top and bottom wrapping and defined as follows:
<wp:anchor … >
…
<wp:wrapTopAndBottom />
</wp:anchor>
The wrapTopAndBottom element specifies that text must wrap around neither side of this object. end
example]
Attributes Description
distB (Distance Specifies the minimum distance which shall be maintained between the bottom edge of
From Text on this drawing object and any subsequent text within the document when this graphical
Bottom Edge) object is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its bottom edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
…
<wp:wrapTopAndBottom distB="457200" … />
</wp:anchor>
The distB attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
distT (Distance Specifies the minimum distance which shall be maintained between the top edge of this
From Text on Top drawing object and any subsequent text within the document when this graphical object
Edge) is displayed within the document's contents.
The distance shall be measured in EMUs (English Metric Units).
[Example: Consider a floating DrawingML object which must have one-half of an inch of
padding between its top edge and the nearest text. This setting would be specified as
follows:
<wp:anchor … >
©ISO/IEC 2016 – All rights reserved 3133\n\n--- Page 3144 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
…
<wp:wrapTopAndBottom distT="457200" … />
</wp:anchor>
The distT attribute specifies that the padding distance must be 457200 EMUs or one-half
of an inch. end example]
The possible values for this attribute are defined by the ST_WrapDistance simple type
(§20.4.3.6).
[Note: The W3C XML Schema definition of this element’s content model (CT_WrapTopBottom) is located in
§A.4.4. end note]
20.4.2.21 bg (Background Formatting)
This element defines formatting that can be applied to the background shape of the document. The background
shape can hold formatting options just as a normal shape can hold within DrawingML.
20.4.2.22 bodyPr (Body Properties)
This element defines the body properties for the text body within a shape.
Attributes Description
anchor (Anchor) Specifies the anchoring position of the txBody within the shape. If this attribute is
omitted, then a value of t, or top is implied.
The possible values for this attribute are defined by the ST_TextAnchoringType simple
type (§20.1.10.60).
anchorCtr (Anchor Specifies the centering of the text box. The way it works fundamentally is to determine
Center) the smallest possible "bounds box" for the text and then to center that "bounds box"
accordingly. This is different than paragraph alignment, which aligns the text within the
"bounds box" for the text. This flag is compatible with all of the different kinds of
anchoring. If this attribute is omitted, then a value of 0 or false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bIns (Bottom Inset) Specifies the bottom inset of the bounding rectangle. Insets are used just as internal
margins for text boxes within shapes. If this attribute is omitted, a value of 45720 or 0.05
inches is implied.
The possible values for this attribute are defined by the ST_Coordinate32 simple type
(§20.1.10.17).
compatLnSpc Specifies that the line spacing for this text body is decided in a simplistic manner using
(Compatible Line the font scene. If this attribute is omitted, a value of 0 or false is implied.
3134 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3145 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Spacing)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
forceAA (Force Forces the text to be rendered anti-aliased regardless of the font size. Certain fonts can
Anti-Alias) appear grainy around their edges unless they are anti-aliased. Therefore this attribute
allows for the specifying of which bodies of text should always be anti-aliased and which
ones should not. If this attribute is omitted, then a value of 0 or false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
fromWordArt Specifies that text within this textbox is converted text from a WordArt object. This is
(From WordArt) more of a backwards compatibility attribute that is useful to the application from a
tracking perspective. WordArt was the former way to apply text effects and therefore
this attribute is useful in document conversion scenarios. If this attribute is omitted, then
a value of 0 or false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
horzOverflow (Text Determines whether the text can flow out of the bounding box horizontally. This is used
Horizontal to determine what happens in the event that the text within a shape is too large for the
Overflow) bounding box it is contained within. If this attribute is omitted, then a value of overflow
is implied.
The possible values for this attribute are defined by the ST_TextHorzOverflowType
simple type (§20.1.10.69).
lIns (Left Inset) Specifies the left inset of the bounding rectangle. Insets are used just as internal margins
for text boxes within shapes. If this attribute is omitted, then a value of 91440 or
0.1 inches is implied.
The possible values for this attribute are defined by the ST_Coordinate32 simple type
(§20.1.10.17).
numCol (Number of Specifies the number of columns of text in the bounding rectangle. When applied to a
Columns) text run this property takes the width of the bounding box for the text and divides it by
the number of columns specified. These columns are then treated as overflow containers
in that when the previous column has been filled with text the next column acts as the
repository for additional text. When all columns have been filled and text still remains
then the overflow properties set for this text body are used and the text is reflowed to
make room for additional text. If this attribute is omitted, then a value of 1 is implied.
The possible values for this attribute are defined by the ST_TextColumnCount simple
type (§20.1.10.65).
rIns (Right Inset) Specifies the right inset of the bounding rectangle. Insets are used just as internal
margins for text boxes within shapes. If this attribute is omitted, then a value of 91440 or
0.1 inches is implied.
©ISO/IEC 2016 – All rights reserved 3135\n\n--- Page 3146 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_Coordinate32 simple type
(§20.1.10.17).
rot (Rotation) Specifies the rotation that is being applied to the text within the bounding box. If it not
specified, the rotation of the accompanying shape is used. If it is specified, then this is
applied independently from the shape. That is the shape can have a rotation applied in
addition to the text itself having a rotation applied to it. If this attribute is omitted, then a
value of 0, is implied.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
rtlCol (Columns Specifies whether columns are used in a right-to-left or left-to-right order. The usage of
Right-To-Left) this attribute only sets the column order that is used to determine which column
overflow text should go to next. If this attribute is omitted, then a value of 0 or falseis
implied in which case text starts in the leftmost column and flow to the right.
[Note: This attribute in no way determines the direction of text but merely the direction
in which multiple columns are used. end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
spcCol (Space Specifies the space between text columns in the text area. This should only apply when
Between Columns) there is more than 1 column present. If this attribute is omitted, then a value of 0 is
implied.
The possible values for this attribute are defined by the ST_PositiveCoordinate32 simple
type (§20.1.10.43).
spcFirstLastPara Specifies whether the before and after paragraph spacing defined by the user is to be
(Paragraph Spacing) respected. While the spacing between paragraphs is helpful, it is additionally useful to be
able to set a flag as to whether this spacing is to be followed at the edges of the text
body, in other words the first and last paragraphs in the text body. More precisely since
this is a text body level property it should only effect the before paragraph spacing of the
first paragraph and the after paragraph spacing of the last paragraph for a given text
body. If this attribute is omitted, then a value of 0, or false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
tIns (Top Inset) Specifies the top inset of the bounding rectangle. Insets are used just as internal margins
for text boxes within shapes. If this attribute is omitted, then a value of 45720 or
0.05 inches is implied.
The possible values for this attribute are defined by the ST_Coordinate32 simple type
(§20.1.10.17).
upright (Text Specifies whether text should remain upright, regardless of the transform applied to it
3136 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3147 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Upright) and the accompanying shape transform. If this attribute is omitted, then a value of 0, or
false is implied.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
vert (Vertical Text) Determines if the text within the given text body should be displayed vertically. If this
attribute is omitted, then a value of horz, or no vertical text is implied.
The possible values for this attribute are defined by the ST_TextVerticalType simple
type (§20.1.10.83).
vertOverflow (Text Determines whether the text can flow out of the bounding box vertically. This is used to
Vertical Overflow) determine what happens in the event that the text within a shape is too large for the
bounding box it is contained within. If this attribute is omitted, then a value of overflow
is implied.
The possible values for this attribute are defined by the ST_TextVertOverflowType
simple type (§20.1.10.84).
wrap (Text Specifies the wrapping options to be used for this text body. If this attribute is omitted,
Wrapping Type) then a value of square is implied which wraps the text using the bounding text box.
The possible values for this attribute are defined by the ST_TextWrappingType simple
type (§20.1.10.85).
20.4.2.23 cNvCnPr (Non-Visual Connector Shape Drawing Properties)
This element specifies the non-visual drawing properties specific to a connector shape. This includes
information specifying the shapes to which the connector shape is connected.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualConnectorProperties) is
located in §A.4.4. end note]
20.4.2.24 cNvContentPartPr (Non-Visual Content Part Drawing Properties)
This element specifies the non-visual drawing properties for a content part. This allows for additional
information that does not affect the appearance of the content part to be stored.
Attributes Description
isComment (Is a Specifies whether the content part is a comment or an annotation. If true, it is a
Comment) comment; otherwise, it is a general annotation.
Namespace: The default value for this attribute is true.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a WordprocessingDrawingML object defined as follows:
ml/main
<… isComment="false">
©ISO/IEC 2016 – All rights reserved 3137\n\n--- Page 3148 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The content part shape does not represent a comment.
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualContentPartProperties) is
located in §A.4.1. end note]
20.4.2.25 cNvFrPr (Non-Visual Graphic Frame Drawing Properties)
This element specifies the non-visual drawing properties for a graphic frame. These non-visual properties are
properties that the generating application would utilize when rendering.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualGraphicFrameProperties)
is located in §A.4.1. end note]
20.4.2.26 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties)
This element specifies the non-visual drawing properties for a group shape. These non-visual properties are
properties that the generating application would utilize when rendering.
20.4.2.27 cNvPr (Non-Visual Drawing Properties)
This element specifies non-visual canvas properties. This allows for additional information that does not affect
the appearance of the picture to be stored.
[Example: Consider the following WordprocessingDrawingML:
<wsp>
…
<cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
…
</wsp>
end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications that do not display the current object.
Namespace: If this element is omitted, then no alternative text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
3138 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3149 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text that can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
Namespace: This attribute determines whether the object is rendered or made hidden. [Note: An
http://purl.oclc.or application can have settings which allow this object to be viewed. end note]
g/ooxml/drawing
ml/main If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
[Example: Consider an inline DrawingML object that must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
Namespace:
http://purl.oclc.or If multiple objects within the same document share the same id attribute value, then the
g/ooxml/drawing document shall be considered non-conformant.
ml/main
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object defined as follows:
©ISO/IEC 2016 – All rights reserved 3139\n\n--- Page 3150 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
g/ooxml/drawing
ml/main < … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
Namespace: If this attribute is omitted, then no title text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
20.4.2.28 cNvSpPr (Non-Visual Drawing Properties for a Shape)
This element specifies the non-visual drawing properties for a shape. These properties are to be used by the
generating application to determine how the shape should be dealt with.
Attributes Description
txBox (Text Box) Specifies that the corresponding shape is a text box and thus should be treated as such
by the generating application. If this attribute is omitted then it is assumed that the
Namespace: corresponding shape is not specifically a text box.
http://purl.oclc.or
g/ooxml/drawing [Note: Because a shape is not specified to be a text box does not mean that it cannot
ml/main have text attached to it. A text box is merely a specialized shape with specific properties.
end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
20.4.2.29 contentPart (Content Part)
This element specifies a reference to XML content in a format not defined by ECMA-376. [Note: This part allows
the native use of other commonly used interchange formats, such as:
3140 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3151 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 MathML (http://www.w3.org/TR/MathML2/)
 SMIL (http://www.w3.org/TR/REC-smil/)
 SVG (http://www.w3.org/TR/SVG11/)
end note]
The relationship type of the explicit relationship specified by this element shall be
http://purl.oclc.org/ooxml/officeDocument/relationships/customXml and have a TargetMode attribute value of
Internal. If an application cannot process content of the content type specified by the targeted part, then it
should continue to process the file. If possible, it should also provide some indication that unknown content was
not imported.
Attributes Description
bwMode (Black and Specifies how to interpret color information contained within a content part to achieve a
White Mode) color, black and white, or grayscale rendering of the content part. This attribute specifies
only the rendering mode applied to the content part; it does not affect how the actual
color information is persisted.
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
id (Relationship to Specifies the relationship ID to a specified part.
Part)
The specified relationship shall match the relationship type required by the parent
Namespace: element:
http://purl.oclc.org/  http://purl.oclc.org/ooxml/officeDocument/customXml for the contentPart
ooxml/officeDocum element
ent/relationships  http://purl.oclc.org/ooxml/officeDocument/relationships/footer for the
footerReference element
 http://purl.oclc.org/ooxml/officeDocument/relationships/header for the
headerReference element
 http://purl.oclc.org/ooxml/officeDocument/relationships/font for the
embedBold, embedBoldItalic, embedItalic, or embedRegular elements
 http://purl.oclc.org/ooxml/officeDocument/relationships/printerSettings for the
printerSettings element
 http://purl.oclc.org/ooxml/officeDocument/relationships/hyperlink for the
longDesc or hyperlink element
[Example: Consider an XML element which has the following id attribute:
<… r:id="rId10" />
The markup specifies the associated relationship part with relationship ID rId1 contains
the corresponding relationship information for the parent XML element. end example]
The possible values for this attribute are defined by the ST_RelationshipId simple type
(§22.8.2.1).
©ISO/IEC 2016 – All rights reserved 3141\n\n--- Page 3152 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_WordprocessingContentPart) is
located in §A.4.4. end note]
20.4.2.30 extLst (Extension List)
This element specifies an extension list, within which all future extensions are defined within ext elements.
The extension list along with corresponding future extensions is used to extend the storage capabilities of the
DrawingML framework. This allows for various new types of data to be stored natively within the existing
diagram syntax.
20.4.2.31 graphicFrame (Graphical object container)
This element specifies a container for a graphical object in WordprocessingML.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicFrame) is located in §A.4.5.
end note]
20.4.2.32 grpSp (Group Shape)
This element specifies a group shape that represents many shapes grouped together. This shape is to be treated
just as if it were a regular shape but instead of being described by a single geometry it is made up of all the
shape geometries encompassed within it. Within a group shape each of the shapes that make up the group are
specified just as they normally would. The idea behind grouping elements however is that a single transform can
apply to many shapes at the same time.
20.4.2.33 grpSpPr (Group Shape Properties)
This element specifies the properties that are to be common across all of the shapes within the corresponding
group. If there are any conflicting properties within the group shape properties and the individual shape
properties then the individual shape properties should take precedence.
Attributes Description
bwMode (Black Specifies that the group shape should be rendered using only black and white coloring.
and White Mode) That is the coloring information for the group shape should be converted to either black
or white when rendering the corresponding shapes.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main [Note: This does not mean that the group shapes themselves are stored with only black
and white color information. This attribute instead sets the rendering mode that the
shapes use when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
3142 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3153 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.34 linkedTxbx (Textual contents of shape)
This element specifies the textual contents of a shape that is not the first in the series of shapes for the same
text box story.
Attributes Description
id (ID) Specifies the identity of the text box story begun by a txbx element. This value shall be
unique across a document for each txbx element.
The possible values for this attribute are defined by the W3C XML Schema
unsignedShort datatype.
seq (sequence Specifies the position of the owning shape in the given text box story.
index)
The possible values for this attribute are defined by the W3C XML Schema
unsignedShort datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ LinkedTextboxInformation) is
located in §A.4.4. end note]
20.4.2.35 spPr (Shape Properties)
This element specifies the visual shape properties that can be applied to a shape. These properties include the
shape fill, outline, geometry, effects, and 3D orientation.
Attributes Description
bwMode (Black and Specifies that the picture should be rendered using only black and white coloring. That is
White Mode) the coloring information for the picture should be converted to either black or white
when rendering the picture.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main [Note: This does not mean that the picture itself that is stored within the file is
necessarily a black and white picture. This attribute instead sets the rendering mode that
the picture has applied to when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
20.4.2.36 style (Shape Style)
This element specifies the style information for a shape. This is used to define a shape's appearance in terms of
the preset styles defined by the style matrix for the theme.
©ISO/IEC 2016 – All rights reserved 3143\n\n--- Page 3154 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.37 txbx (Textual contents of shape)
This element specifies the textual contents of a shape which is the first in the series of shapes for the same text
box story. This element shall be present only in the CT_WordprocessingShape element that is the first in a
series of CT_WordprocessingShape elements that refer to the same text box story.
Attributes Description
id (ID) Specifies the identity of the text box story begun by a txbx element. This value shall be
unique across a document for each txbx element.
The possible values for this attribute are defined by the W3C XML Schema
unsignedShort datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextboxInfo) is located in §A.4.4.
end note]
20.4.2.38 txbxContent (Rich Text Box Content Container)
This element specifies that its contents shall be any rich WordprocessingML content, and that this content is the
rich contents of a drawing object defined using DrawingML syntax.
If this element contains within any of its contents any of the following content, then the document shall be
considered non-conformant:
 References to other WordprocessingML document stories (comments, footnotes, endnotes)
 Vector Markup Language (VML)
 Additional txbxContent elements (as part of nested DrawingML objects)
20.4.2.39 wgp (WordprocessingML Shape Group)
This element specifies a shape group in WordprocessingML.
[Note: The W3C XML Schema definition of this element’s content model (CT_ WordprocessingGroup) is located
in §A.4.5. end note]
20.4.2.40 whole (Whole E2O Formatting)
Formatting that applies to the entire diagram object, and not just the background, includes line and effect
properties.
20.4.2.41 wpc (WordprocessingML Drawing Canvas)
This element specifies a drawing canvas in WordprocessingML. A drawing canvas is a logical grouping of shapes.
[Note: A Drawing Canvas is typically used to allow grouping of shapes together for bulk operations. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_ WordprocessingCanvas) is located
in §A.4.5. end note]
3144 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3155 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.4.2.42 wsp (WordprocessingML Shape)
This element specifies a shape in WordprocessingML.
Attributes Description
normalEastAsianFl Specifies that the text flow of the text contents of the shape shall ignore the text flow
ow (East Asian value specified by the vert attribute of the bodyPr element.
Flow)
If this attribute is set to TRUE then the text flows in the manner specified by the value
"tbV" for ST_TextDirection (§17.18.93).
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ WordprocessingShape) is located
in §A.4.5. end note]
20.4.2.43 xfrm (2D Transform for Graphic Frames)
This element specifies a two dimensional transform for a Graphic Frame.
Attributes Description
flipH (Horizontal Specifies a horizontal flip. When true, this attribute defines that the shape is flipped
Flip) horizontally about the center of its bounding box.
Namespace: [Example: The following illustrates the effect of a horizontal flip.
http://purl.oclc.or
g/ooxml/drawing
ml/main
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
flipV (Vertical Flip) Specifies a vertical flip. When true, this attribute defines that the group is flipped
vertically about the center of its bounding box.
Namespace:
http://purl.oclc.or [Example: The following illustrates the effect of a vertical flip.
g/ooxml/drawing
ml/main
end example]
©ISO/IEC 2016 – All rights reserved 3145\n\n--- Page 3156 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
rot (Rotation) Specifies the rotation of the Graphic Frame. The units for which this attribute is specified
in reside within the simple type definition referenced below.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_Angle simple type
g/ooxml/drawing (§20.1.10.3).
ml/main
20.4.3 Simple Types
This is the complete list of simple types dedicated to DrawingML – WordprocessingML Drawing.
20.4.3.1 ST_AlignH (Relative Horizontal Alignment Positions)
This simple type contains the possible settings specifying how a DrawingML object can be horizontally aligned
relative to the horizontal alignment base defined by the parent element.
[Example: Consider a picture in a WordprocessingML document which has been aligned relative to the edge of
the page - the left of the page horizontally, and the top of the page vertically. This alignment would be specified
as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:align>left</wp:align>
</wp:positionH>
…
</wp:anchor>
The align element with a value of left specifies that for the horizontal positioning defined by the parent
element (in this case, positioning relative to the page), the picture must be aligned to the left edge of the page.
end example]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
center (Center Alignment) Specifies that the object shall be centered with respect
to the horizontal alignment base.
[Example: Centered on the page. end example]
inside (Inside) Specifies that the object shall be inside of the
horizontal alignment base.
3146 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3157 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
[Example: Inside the outside margin. end example]
left (Left Alignment) Specifies that the object shall be left aligned to the
horizontal alignment base.
[Example: Left aligned relative to the margins. end
example]
outside (Outside) Specifies that the object shall be outside of the
horizontal alignment base.
[Example: Outside the left margin. end example]
right (Right Alignment) Specifies that the object shall be right aligned to the
horizontal alignment base.
[Example: Right aligned relative to the margins. end
example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AlignH) is located in §A.4.4. end
note]
20.4.3.2 ST_AlignV (Vertical Alignment Definition)
This simple type contains the possible settings specifying how a DrawingML object can be vertically aligned
relative to the vertical alignment base defined by the parent element.
[Example: Consider a picture in a WordprocessingML document which has been aligned relative to the edge of
the page - the left of the page horizontally, and the top of the page vertically. This alignment would be specified
as follows:
<wp:anchor … >
<wp:positionV relativeFrom="page">
<wp:align>top</wp:align>
</wp:positionH>
…
</wp:anchor>
The align element with a value of top specifies that for the vertical positioning defined by the parent element
(in this case, positioning relative to the page), the picture must be aligned to the top edge of the page. end
example]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
©ISO/IEC 2016 – All rights reserved 3147\n\n--- Page 3158 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bottom (Bottom) Specifies that the object shall be at the bottom of the
vertical alignment base.
[Example: Bottom of the page. end example]
center (Center Alignment) Specifies that the object shall be centered with respect
to the vertical alignment base.
[Example: Centered on the page. end example]
inside (Inside) Specifies that the object shall be inside of the
horizontal alignment base.
[Example: Inside the top margin. end example]
outside (Outside) Specifies that the object shall be outside of the vertical
alignment base.
[Example: Outside the top margin. end example]
top (Top) Specifies that the object shall be at the top of the
vertical alignment base.
[Example: Top of the page. end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_AlignV) is located in §A.4.4. end
note]
20.4.3.3 ST_PositionOffset (Absolute Position Offset Value)
This simple type represents a one dimensional distance which shall be used to offset an objet from its base
positioning location stored in EMUs.
[Example: Consider a DrawingML picture which must be displayed one inch from the top of the page, and one-
half of an inch from the left edge of the page. This object would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:posOffset>914400</wp:posOffset>
</wp:positionH>
<wp:positionV relativeFrom="page">
<wp:posOffset>457200</wp:posOffset>
</wp:positionV>
</wp:anchor>
3148 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3159 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The posOffset element specifies the absolute positioning of the object relative to the top-left edge of the page
in EMUs. end example]
This simple type's contents are a restriction of the W3C XML Schema int datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PositionOffset) is located in
§A.4.4. end note]
20.4.3.4 ST_RelFromH (Horizontal Relative Positioning)
This simple type specifies the possible values for the base from which the relative horizontal positioning of an
object shall be calculated.
[Example: Consider a DrawingML picture which must be displayed at the bottom center of the page. This object
would be specified as follows:
<wp:anchor … >
<wp:positionH relativeFrom="page">
<wp:align>center</wp:align>
</wp:positionH>
…
</wp:anchor>
The relativeFrom attribute specifies that the object is horizontally positioned relative to the page. end
example]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
character (Character) Specifies that the horizontal positioning shall be
relative to the position of the anchor within its run
content.
column (Column) Specifies that the horizontal positioning shall be
relative to the extents of the column which contains its
anchor.
insideMargin (Inside Margin) Specifies that the horizontal positioning shall be
relative to the inside margin of the current page (the
left margin on odd pages, right on even pages).
leftMargin (Left Margin) Specifies that the horizontal positioning shall be
relative to the left margin of the page.
margin (Page Margin) Specifies that the horizontal positioning shall be
relative to the page margins.
outsideMargin (Outside Margin) Specifies that the horizontal positioning shall be
relative to the outside margin of the current page (the
©ISO/IEC 2016 – All rights reserved 3149\n\n--- Page 3160 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
right margin on odd pages, left on even pages).
page (Page Edge) Specifies that the horizontal positioning shall be
relative to the edge of the page.
rightMargin (Right Margin) Specifies that the horizontal positioning shall be
relative to the right margin of the page.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_RelFromH) is located in §A.4.4.
end note]
20.4.3.5 ST_RelFromV (Vertical Relative Positioning)
This simple type specifies the possible values for the base from which the relative vertical positioning of an
object shall be calculated.
[Example: Consider a DrawingML picture which must be displayed at the bottom center of the page. This object
would be specified as follows:
<wp:anchor … >
<wp:positionV relativeFrom="page">
<wp:align>bottom</wp:align>
</wp:positionV>
…
</wp:anchor>
The relativeFrom attribute specifies that the object is horizontally positioned relative to the page. end
example]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bottomMargin (Bottom Margin) Specifies that the vertical positioning shall be relative
to the bottom margin of the current page.
insideMargin (Inside Margin) Specifies that the vertical positioning shall be relative
to the inside margin of the current page.
line (Line) Specifies that the vertical positioning shall be relative
to the line containing the anchor character.
margin (Page Margin) Specifies that the vertical positioning shall be relative
to the page margins.
outsideMargin (Outside Margin) Specifies that the vertical positioning shall be relative
to the outside margin of the current page.
page (Page Edge) Specifies that the vertical positioning shall be relative
3150 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3161 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
to the edge of the page.
paragraph (Paragraph) Specifies that the vertical positioning shall be relative
to the paragraph which contains the drawing anchor.
topMargin (Top Margin) Specifies that the vertical positioning shall be relative
to the top margin of the current page.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_RelFromV) is located in §A.4.4.
end note]
20.4.3.6 ST_WrapDistance (Distance from Text)
This simple type represents a one dimensional distance which shall be used to offset an object from text, stored
in EMUs.
[Example: Consider a floating DrawingML object which must have one-half of an inch of padding between its left
edge and the nearest text. This setting would be specified as follows:
<wp:anchor … >
…
<wp:wrapThrough distL="457200" … />
</wp:anchor>
The distL attribute specifies that the padding distance must be 457200 EMUs or one-half of an inch. end
example]
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_WrapDistance) is located in
§A.4.4. end note]
20.4.3.7 ST_WrapText (Text Wrapping Location)
This simple type specifies the possible settings for how text can wrap around the object's left and right sides.
[Example: Consider a floating DrawingML object which must allow text to wrap around its left side only. This
setting would be specified as follows:
<wp:anchor … >
…
<wp:wrapTight wrapText="left" … />
</wp:anchor>
The wrapText attribute value of left specifies that text must only wrap around the let side of the object. end
example]
©ISO/IEC 2016 – All rights reserved 3151\n\n--- Page 3162 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bothSides (Both Sides) Specifies that text shall wrap around both sides of the
object.
largest (Largest Side Only) Specifies that text shall only wrap around the largest
side of the object.
If the object is positioned in the exact center of the
page, the text shall wrap around the side on which text
is first encountered:
 If the first line of text intersecting the object is
using left-to-right reading order, the text shall
wrap to the object's left.
 If the first line of text intersecting the object is
using right-to-left reading order, the text shall
wrap to the object's right.
left (Left Side Only) Specifies that text shall only wrap around the left side
of the object.
right (Right Side Only) Specifies that text shall only wrap around the right side
of the object.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_WrapText) is located in §A.4.4.
end note]
20.5 DrawingML - SpreadsheetML Drawing
Within a SpreadsheetML document, it is possible to include graphical DrawingML objects:
 Pictures (§20.2)
 Locked Canvases (§20.3)
 Diagrams (§21.4)
 Charts (§21.2)
When these objects are present in a spreadsheet document, it is necessary to include information which
specifies how the objects shall be positioned relative to the parent worksheet. [Example: Whether the object is
anchored to a specific row, whether it resizes with cells, and so on. end example]
The SpreadsheetML Drawing namespace acts in this capacity, specifying all information necessary to anchor and
display DrawingML objects within a spreadsheet document.
[Example: Consider a DrawingML picture which must be anchored to a specific cell for its top left and bottom
right corners, resizing as those cells are relocated. This object would be specified as follows:
3152 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3163 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xdr:twoCellAnchor>
<xdr:from>
…
</xdr:from>
<xdr:to>
…
</xdr:to>
<xdr:graphicFrame>
…
<a:graphic>
<a:graphicData
uri="http://purl.oclc.org/ooxml/drawingml/diagram">
<dgm:relIds xmlns:dgm="…" xmlns:r="…" r:dm="rId1" r:lo="rId2"
r:qs="rId3" r:cs="rId4" />
</a:graphicData>
</a:graphic>
</xdr:graphicFrame>
</xdr:twoCellAnchor>
The twoCellAnchor element (§20.5.2.33) specifies that this object anchored to the cells specified by the to
(§20.5.2.32) and from (§20.5.2.15) elements. end example]
20.5.1 Table of Contents
This subclause is informative.
20.5.2 Elements .................................................................................................................................... 3154
20.5.2.1 absoluteAnchor (Absolute Anchor Shape Size) ........................................................................... 3154
20.5.2.2 blipFill (Picture Fill) ...................................................................................................................... 3154
20.5.2.3 clientData (Client Data) ............................................................................................................... 3157
20.5.2.4 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties) ................................................ 3157
20.5.2.5 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties) ....................................... 3157
20.5.2.6 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties) ....................................................... 3157
20.5.2.7 cNvPicPr (Non-Visual Picture Drawing Properties) ..................................................................... 3158
20.5.2.8 cNvPr (Non-Visual Drawing Properties) ...................................................................................... 3159
20.5.2.9 cNvSpPr (Connection Non-Visual Shape Properties) ................................................................... 3161
20.5.2.10 col (Column)) ............................................................................................................................... 3161
20.5.2.11 colOff (Column Offset) ................................................................................................................. 3162
20.5.2.12 contentPart (Content Part) .......................................................................................................... 3162
20.5.2.13 cxnSp (Connection Shape) ........................................................................................................... 3166
20.5.2.14 ext (Shape Extent) ....................................................................................................................... 3166
20.5.2.15 from (Starting Anchor Point) ....................................................................................................... 3167
20.5.2.16 graphicFrame (Graphic Frame) .................................................................................................... 3168
20.5.2.17 grpSp (Group Shape) ................................................................................................................... 3169
20.5.2.18 grpSpPr (Group Shape Properties) .............................................................................................. 3170
20.5.2.19 nvCxnSpPr (Non-Visual Properties for a Connection Shape) ...................................................... 3170
©ISO/IEC 2016 – All rights reserved 3153\n\n--- Page 3164 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.5.2.20 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame) ............................................... 3170
20.5.2.21 nvGrpSpPr (Non-Visual Properties for a Group Shape) ............................................................... 3170
20.5.2.22 nvPicPr (Non-Visual Properties for a Picture) .............................................................................. 3171
20.5.2.23 nvSpPr (Non-Visual Properties for a Shape) ................................................................................ 3171
20.5.2.24 oneCellAnchor (One Cell Anchor Shape Size) .............................................................................. 3171
20.5.2.25 pic (Picture) .................................................................................................................................. 3171
20.5.2.26 pos (Position) ............................................................................................................................... 3173
20.5.2.27 row (Row) .................................................................................................................................... 3173
20.5.2.28 rowOff (Row Offset) .................................................................................................................... 3173
20.5.2.29 sp (Shape) .................................................................................................................................... 3174
20.5.2.30 spPr (Shape Properties) ............................................................................................................... 3175
20.5.2.31 style (Shape Style) ....................................................................................................................... 3175
20.5.2.32 to (Ending Anchor Point) ............................................................................................................. 3175
20.5.2.33 twoCellAnchor (Two Cell Anchor Shape Size) ............................................................................. 3176
20.5.2.34 txBody (Shape Text Body) ............................................................................................................ 3177
20.5.2.35 wsDr (Worksheet Drawing) ......................................................................................................... 3177
20.5.2.36 xfrm (2D Transform for Graphic Frames) .................................................................................... 3177
20.5.3 Simple Types .............................................................................................................................. 3178
20.5.3.1 ST_ColID (Column ID) .................................................................................................................. 3178
20.5.3.2 ST_EditAs (Resizing Behaviors) .................................................................................................... 3178
20.5.3.3 ST_RowID (Row ID) ...................................................................................................................... 3179
End of informative text.
20.5.2 Elements
The following elements define the contents of the Spreadsheet Drawing namespace:
20.5.2.1 absoluteAnchor (Absolute Anchor Shape Size)
This element is used as an anchor placeholder for a shape or group of shapes. It anchors the object in the same
position relative to sheet position and its extents are in EMU units.
[Note: The W3C XML Schema definition of this element’s content model (CT_AbsoluteAnchor) is located in
§A.4.5. end note]
20.5.2.2 blipFill (Picture Fill)
This element specifies the type of picture fill that the picture object has. Because a picture has a picture fill
already by default, it is possible to have two fills specified for a picture object. An example of this is shown
below.
[Example: Consider the picture below that has a blip fill applied to it. The image used to fill this picture object
has transparent pixels instead of white pixels.
<xdr:pic>
..
3154 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3165 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xdr:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</xdr:blipFill>
..
</xdr:pic>
The above picture object is shown as an example of this fill type. end example]
[Example: Consider now the same picture object but with an additional gradient fill applied within the shape
properties portion of the picture.
<xdr:pic>
..
<xdr:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</xdr:blipFill>
<xdr:spPr>
<a:gradFill>
<a:gsLst>
<a:gs pos="0">
<a:schemeClr val="tx2">
<a:shade val="50000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="39999">
<a:schemeClr val="tx2">
©ISO/IEC 2016 – All rights reserved 3155\n\n--- Page 3166 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:tint val="20000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="70000">
<a:srgbClr val="C4D6EB"/>
</a:gs>
<a:gs pos="100000">
<a:schemeClr val="bg1"/>
</a:gs>
</a:gsLst>
</a:gradFill>
</xdr:spPr>
..
</xdr:pic>
The above picture object is shown as an example of this double fill type. end example]
Attributes Description
dpi (DPI Setting) Specifies the DPI (dots per inch) used to calculate the size of the blip. If not present or
zero, the DPI in the blip is used.
Namespace:
http://purl.oclc.or [Note: This attribute is primarily used to keep track of the picture quality within a
g/ooxml/drawing document. There are different levels of quality needed for print than on-screen viewing
ml/main and thus a need to track this information. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
rotWithShape Specifies that the fill should rotate with the shape. That is, when the shape that has been
(Rotate With Shape) filled with a picture and the containing shape (say a rectangle) is transformed with a
rotation then the fill is transformed with the same rotation.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the W3C XML Schema boolean
3156 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3167 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
g/ooxml/drawing datatype.
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_BlipFillProperties) is located in
§A.4.1. end note]
20.5.2.3 clientData (Client Data)
This element is used to set certain properties related to a drawing element on the client spreadsheet
application.
Attributes Description
fLocksWithSheet This attribute indicates whether to disable selection on drawing elements when the sheet
(Locks With Sheet is protected.
Flag)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
fPrintsWithSheet This attribute indicates whether to print drawing elements when printing the sheet.
(Prints With Sheet
Flag) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_AnchorClientData) is located in
§A.4.5. end note]
20.5.2.4 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties)
This element specifies the non-visual properties for a connector shape. These are the set of properties on a
shape which do not affect its display within a spreadsheet.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualConnectorProperties) is
located in §A.4.1. end note]
20.5.2.5 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties)
This element specifies the non-visual properties for a single graphical object frame within a spreadsheet. These
are the set of properties of a frame which do not affect its display within a spreadsheet.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualGraphicFrameProperties)
is located in §A.4.1. end note]
20.5.2.6 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties)
This element specifies the non-visual properties of a hierarchical grouping of shapes, graphical object frames,
and child groups. These are the set of properties of a group which do not affect its display within a spreadsheet.
©ISO/IEC 2016 – All rights reserved 3157\n\n--- Page 3168 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model
(CT_NonVisualGroupDrawingShapeProps) is located in §A.4.1. end note]
20.5.2.7 cNvPicPr (Non-Visual Picture Drawing Properties)
This element describes the non-visual properties of a picture within a spreadsheet. These are the set of
properties of a picture which do not affect its display within a spreadsheet.
[Example: Consider the following SpreadsheetDrawingML.
<xdr:pic>
..
<xdr:nvPicPr>
<xdr:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
<xdr:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</xdr:cNvPicPr>
<xdr:nvPr/>
</xdr:nvPicPr>
..
</xdr:pic>
The above example defines some non-visual picture drawing properties for the inserted picture. end example]
Attributes Description
preferRelativeResi Specifies if the user interface should show the resizing of the picture based on the
ze (Relative Resize picture's current size or its original size. If this attribute is set to true, then scaling is
Preferred) relative to the original picture size as opposed to the current picture size.
Namespace: [Example: Consider the case where a picture has been resized within a document and is
http://purl.oclc.or now 50% of the originally inserted picture size. Now if the user chooses to make a later
g/ooxml/drawing adjustment to the size of this picture within the generating application, then the value of
ml/main this attribute should be checked.
If this attribute is set to true then a value of 50% is shown. Similarly, if this attribute is set
to false, then a value of 100% should be shown because the picture has not yet been
resized from its current (smaller) size. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualPictureProperties) is
located in §A.4.1. end note]
3158 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3169 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.5.2.8 cNvPr (Non-Visual Drawing Properties)
This element specifies the set of non-visual properties for the parent element. These properties specify all the
data about the parent which does not affect its display within the spreadsheet.
[Example: Consider the following SpreadSheetDrawingML.
<xdr:pic>
..
<xdr:nvPicPr>
<xdr:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
</xdr:nvPicPr>
..
</xdr:pic>
The above example defines some non-visual drawing properties for the inserted picture. end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications which do not display the current object.
Namespace: If this element is omitted, then no alternative text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text which can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
Namespace: This attribute determines whether the object is rendered or made hidden. [Note: An
http://purl.oclc.or application can have settings which allow this object to be viewed. end note]
g/ooxml/drawing
ml/main If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
[Example: Consider an inline DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
©ISO/IEC 2016 – All rights reserved 3159\n\n--- Page 3170 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
Namespace:
http://purl.oclc.or If multiple objects within the same document share the same id attribute value, then the
g/ooxml/drawing document shall be considered non-conformant.
ml/main
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object defined as follows:
g/ooxml/drawing
ml/main < … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
Namespace: If this attribute is omitted, then no title text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
3160 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3171 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
20.5.2.9 cNvSpPr (Connection Non-Visual Shape Properties)
This element specifies the set of non-visual properties for a connection shape. These properties specify all data
about the connection shape which do not affect its display within a spreadsheet.
[Example: Consider the shape that has a shape lock applied to it.
<xdr:sp>
<xdr:nvSpPr>
<xdr:cNvPr id="2" name="Rectangle 1"/>
<xdr:cNvSpPr>
<a:spLocks noGrp="1"/>
</xdr:cNvSpPr>
</xdr:nvSpPr>
..
</xdr:sp>
This shape lock is stored within the non-visual drawing properties for this shape. end example]
Attributes Description
txBox (Text Box) Specifies that the corresponding shape is a text box and thus should be treated as such
by the generating application. If this attribute is omitted then it is assumed that the
Namespace: corresponding shape is not specifically a text box.
http://purl.oclc.or
g/ooxml/drawing [Note: Because a shape is not specified to be a text box does not mean that it cannot
ml/main have text attached to it. A text box is merely a specialized shape with specific properties.
end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingShapeProps) is
located in §A.4.1. end note]
20.5.2.10 col (Column))
This element specifies the column that is used within the from and to elements to specify anchoring information
for a shape within a spreadsheet
The possible values for this element are defined by the ST_ColID simple type (§20.5.3.1).
[Note: The W3C XML Schema definition of this element’s content model (ST_ColID) is located in §A.4.5. end
note]
©ISO/IEC 2016 – All rights reserved 3161\n\n--- Page 3172 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.5.2.11 colOff (Column Offset)
This element is used to specify the column offset within a cell. The units for which this attribute is specified in
reside within the simple type definition referenced below.
The possible values for this element are defined by the ST_Coordinate simple type (§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (ST_Coordinate) is located in §A.4.1.
end note]
20.5.2.12 contentPart (Content Part)
This element specifies a reference to XML content in a format not defined by ISO/IEC 29500. [Note: This part
allows the native use of other commonly used interchange formats, such as:
 MathML (http://www.w3.org/TR/MathML2/)
 SMIL (http://www.w3.org/TR/REC-smil/)
 SVG (http://www.w3.org/TR/SVG11/)
end note]
The relationship type of the explicit relationship specified by this element shall be
http://purl.oclc.org/ooxml/officeDocument/relationships/customXml and have a TargetMode attribute value of
Internal. If an application cannot process content of the content type specified by the targeted part, then it
should continue to process the file. If possible, it should also provide some indication that unknown content was
not imported.
[Example: Consider a SpreadsheetML document which includes the following SVG markup in a part named
svg1.xml:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!--======================================================================-->
<!--= Copyright 2000 World Wide Web Consortium, (Massachusetts =-->
<!--= Institute of Technology, Institut National de Recherche en =-->
<!--= Informatique et en Automatique, Keio University). All Rights =-->
<!--= Reserved. See http://www.w3.org/Consortium/Legal/. =-->
<!--======================================================================-->
<!-- =====================================================================-->
<!-- -->
<!-- color-datatypes-BE-01.svg -->
<!-- renamed for 1.1 suite to color-prop-02-f.svg -->
<!-- -->
<!-- Author : Chris Lilley, 12-Aug-2000 -->
<!-- 1.1 revision by Rick Graham -->
3162 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3173 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<!-- Revised for SVGT/B: Benoit Bezaire Jul/02/2002 -->
<!-- More revision CL -->
<!--======================================================================-->
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink" id="svg-root" width="100%"
height="100%" viewBox="0 0 480 360">
<title id="test-title">color-prop-02-f.svg</title>
<desc id="test-desc">Test that viewer has the basic capability to render
X11colors, using any of the equivalent forms.</desc>
<!--================================================================-->
<!--Content of Test Case follows… ===============-->
<!--================================================================-->
<g id="test-body-content">
<!-- groups of five colors -->
<g>
<circle cx="75" cy="40" r="20" fill="crimson"/>
<circle cx="115" cy="40" r="20" fill="#DC143C"/>
<circle cx="75" cy="80" r="20" fill="rgb(220,20,60)"/>
<circle cx="115" cy="80" r="20"
fill="rgb(86.274509803921568627450980392157%,7.8431372549019607843137254901961%,
23.529411764705882352941176470588%)"/>
</g>
<g>
<circle cx="200" cy="40" r="20" fill="palegreen"/>
<circle cx="240" cy="40" r="20" fill="#98FB98"/>
<circle cx="200" cy="80" r="20" fill="rgb(152, 251, 152)"/>
<circle cx="240" cy="80" r="20"
fill="rgb(59.60784313725490196078431372549%,98.431372549019607843137254901961%,5
9.60784313725490196078431372549%)"/>
</g>
<g>
<circle cx="325" cy="40" r="20" fill="royalblue"/>
<circle cx="365" cy="40" r="20" fill="#4169E1"/>
<circle cx="325" cy="80" r="20" fill="rgb(65, 105, 225)"/>
<circle cx="365" cy="80" r="20"
fill="rgb(25.490196078431372549019607843137%,41.176470588235294117647058823529%,
88.235294117647058823529411764706%)"/>
</g>
<g>
<circle cx="75" cy="135" r="20" fill="firebrick"/>
<circle cx="115" cy="135" r="20" fill="#B22222"/>
<circle cx="75" cy="175" r="20" fill="rgb(178,34,34)"/>
©ISO/IEC 2016 – All rights reserved 3163\n\n--- Page 3174 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<circle cx="115" cy="175" r="20"
fill="rgb(69.803921568627450980392156862745%,13.333333333333333333333333333333%,
13.333333333333333333333333333333%)"/>
</g>
<g>
<circle cx="200" cy="135" r="20" fill="seagreen"/>
<circle cx="240" cy="135" r="20" fill="#2E8B57"/>
<circle cx="200" cy="175" r="20" fill="rgb(46, 139, 87)"/>
<circle cx="240" cy="175" r="20"
fill="rgb(18.039215686274509803921568627451%,54.509803921568627450980392156863%,
34.117647058823529411764705882353%)"/>
</g>
<g>
<circle cx="325" cy="135" r="20" fill="mediumblue"/>
<circle cx="365" cy="135" r="20" fill="#0000CD"/>
<circle cx="325" cy="175" r="20" fill="rgb(0, 0, 205)"/>
<circle cx="365" cy="175" r="20"
fill="rgb(0%,0%,80.39215686274509803921568627451%)"/>
</g>
<g>
<circle cx="75" cy="230" r="20" fill="indianred"/>
<circle cx="115" cy="230" r="20" fill="#CD5C5C"/>
<circle cx="75" cy="270" r="20" fill="rgb(205, 92, 92)"/>
<circle cx="115" cy="270" r="20"
fill="rgb(80.39215686274509803921568627451%,36.078431372549019607843137254902%,3
6.078431372549019607843137254902%)"/>
</g>
<g>
<circle cx="200" cy="230" r="20" fill="lawngreen"/>
<circle cx="240" cy="230" r="20" fill="#7CFC00"/>
<circle cx="200" cy="270" r="20" fill="rgb(124, 252, 0)"/>
<circle cx="240" cy="270" r="20"
fill="rgb(48.627450980392156862745098039216%,98.823529411764705882352941176471%,
0%)"/>
</g>
<g>
<circle cx="325" cy="230" r="20" fill="mediumturquoise"/>
<circle cx="365" cy="230" r="20" fill="#48D1CC"/>
<circle cx="325" cy="270" r="20" fill="rgb(72, 209, 204)"/>
<circle cx="365" cy="270" r="20"
fill="rgb(28.235294117647058823529411764706%,81.960784313725490196078431372549%,
80%)"/>
</g>
3164 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3175 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</g>
<text id="revision" x="10" y="340" font-size="40" stroke="none"
fill="black">$Revision: 1.6 $</text>
<rect id="test-frame" x="1" y="1" width="478" height="358" fill="none"
stroke="#000000"/>
</svg>
The SpreadsheetML Drawing part would reference this content as follows:
<wsDr>
<twoCellAnchor>
<from>
<col>3</col>
<colOff>152400</colOff>
<row>5</row>
<rowOff>123825</rowOff>
</from>
<to>
<col>8</col>
<colOff>266700</colOff>
<row>22</row>
<rowOff>38100</rowOff>
</to>
</twoCellAnchor>
<contentPart r:id="svg1"/>
</wsDr>
The contentPart element specifies that the SVG markup targeted by the relationship with an ID of svg1 is part
of the SpreadsheetML document. Examining the contents of the corresponding relationship part item, we can
see the targets for that relationship:
<Relationships … >
…
<Relationship Id="svg1" TargetMode="Internal"
Type="http://purl.oclc.org/ooxml/officeDocument/relationships/customXml"
Target="svg1.xml" />
…
</Relationships>
The corresponding relationship part item shows that the file to be imported is named svg1.xml. end example]
Attributes Description
id (Relationship to Specifies the relationship ID to a content part.
Part)
[Example: Consider an XML element which has the following id attribute:
©ISO/IEC 2016 – All rights reserved 3165\n\n--- Page 3176 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Namespace:
http://purl.oclc.or <… r:id="rId1" />
g/ooxml/officeDoc
ument/relationshi The markup specifies the associated relationship part with relationship ID rId1 contains
ps the corresponding relationship information for the parent XML element. end example]
The possible values for this attribute are defined by the ST_RelationshipId simple type
(§22.8.2.1).
[Note: The W3C XML Schema definition of this element’s content model (CT_Rel) is located in §A.4.5. end note]
20.5.2.13 cxnSp (Connection Shape)
This element specifies the properties for a connection shape drawing element. A connection shape is a line, etc.
that connects two other shapes in this drawing.
Attributes Description
fPublished (Publish This attribute indicates whether the shape shall be published with the worksheet when
to Server Flag) sent to the server.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
macro (Reference This element specifies the custom function associated with the object. [Example: A macro
to Custom Function) script, add-in function, and so on. end example]
The format of this string shall be application-defined, and should be ignored if not
understood.
[Example:
< … macro="DoWork()" />
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Connector) is located in §A.4.5. end
note]
20.5.2.14 ext (Shape Extent)
This element describes the length and width properties for how far a drawing element should extend for.
3166 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3177 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main <… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main < … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
20.5.2.15 from (Starting Anchor Point)
This element specifies the first anchor point for the drawing element. This is used to anchor the top and left
sides of the shape within the spreadsheet. That is when the cell that is specified in the from element is adjusted,
the shape is also adjusted.
[Example: Consider the following SpreadsheetDrawingML
<xdr:twoCellAnchor>
<xdr:from>
<xdr:col>3</xdr:col>
<xdr:colOff>447675</xdr:colOff>
<xdr:row>8</xdr:row>
<xdr:rowOff>28575</xdr:rowOff>
</xdr:from>
<xdr:to>
©ISO/IEC 2016 – All rights reserved 3167\n\n--- Page 3178 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xdr:col>5</xdr:col>
<xdr:colOff>466725</xdr:colOff>
<xdr:row>14</xdr:row>
<xdr:rowOff>9525</xdr:rowOff>
</xdr:to>
<xdr:sp macro="" textlink="">
…
</xdr:sp>
<xdr:clientData/>
</xdr:twoCellAnchor>
The above example shows the first anchor point being specified via the from element. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Marker) is located in §A.4.5. end
note]
20.5.2.16 graphicFrame (Graphic Frame)
This element describes a single graphical object frame for a spreadsheet which contains a graphical object.
Attributes Description
fPublished (Publish This attribute indicates whether the shape shall be published with the worksheet when
to Server Flag) sent to the server.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
macro (Reference This element specifies the custom function associated with the object. [Example: A macro
To Custom script, add-in function, and so on. end example]
Function)
The format of this string shall be application-defined, and should be ignored if not
understood.
[Example:
< … macro="DoWork()" />
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectFrame) is located in
§A.4.5. end note]
3168 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 3179 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.5.2.17 grpSp (Group Shape)
This element specifies a group shape that represents many shapes grouped together. This shape is to be treated
just as if it were a regular shape but instead of being described by a single geometry it is made up of all the
shape geometries encompassed within it. Within a group shape each of the shapes that make up the group are
specified just as they normally would. The idea behind grouping elements however is that a single transform can
apply to many shapes at the same time.
[Example: Consider the following group shape.
<xdr:grpSp>
<xdr:nvGrpSpPr>
<xdr:cNvPr id="10" name="Group 9"/>
<xdr:cNvGrpSpPr/>
<xdr:nvPr/>
</xdr:nvGrpSpPr>
<xdr:grpSpPr>
<a:xfrm>
<a:off x="838200" y="990600"/>
<a:ext cx="2426208" cy="978408"/>
<a:chOff x="838200" y="990600"/>
<a:chExt cx="2426208" cy="978408"/>
</a:xfrm>
</xdr:grpSpPr>
<xdr:sp>
..
</xdr:sp>
<xdr:sp>
..
</xdr:sp>
<xdr:sp>
..
</xdr:sp>
</xdr:grpSp>
In the above example we see three shapes specified within a single group. These three shapes have their
position and sizes specified just as they normally would within the shape tree. The generating application should
apply the transformation after the bounding box for the group shape has been calculated. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShape) is located in §A.4.5.
end note]
©ISO/IEC 2016 – All rights reserved 3169\n\n--- Page 3180 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
20.5.2.18 grpSpPr (Group Shape Properties)
This element specifies the properties that are to be common across all of the shapes within the corresponding
group. If there are any conflicting properties within the group shape properties and the individual shape
properties then the individual shape properties should take precedence.
Attributes Description
bwMode (Black and Specifies that the group shape should be rendered using only black and white coloring.
White Mode) That is the coloring information for the group shape should be converted to either black
or white when rendering the corresponding shapes.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main [Note: This does not mean that the group shapes themselves are stored with only black
and white color information. This attribute instead sets the rendering mode that the
shapes use when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShapeProperties) is located
in §A.4.1. end note]
20.5.2.19 nvCxnSpPr (Non-Visual Properties for a Connection Shape)
This element specifies all non-visual properties for a connection shape. This element is a container for the non-
visual identification properties, shape properties and application properties that are to be associated with a
connection shape. This allows for additional information that does not affect the appearance of the connection
shape to be stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_ConnectorNonVisual) is located in
§A.4.5. end note]
20.5.2.20 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame)
This element specifies all non-visual properties for a graphic frame. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a graphic
frame. This allows for additional information that does not affect the appearance of the graphic frame to be
stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectFrameNonVisual) is
located in §A.4.5. end note]
20.5.2.21 nvGrpSpPr (Non-Visual Properties for a Group Shape)
This element specifies all non-visual properties for a group shape. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a group
3170 ©ISO/IEC 2016 – All rights reserved\n