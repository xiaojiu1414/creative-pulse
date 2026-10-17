# Evaluator walkthrough

## Open the prototype

1. Open [Creative Pulse](https://creative.segpulse.cn/).
2. Sign in using the dedicated evaluator login supplied privately with the
   competition submission.
3. Open the creative library and select a completed example.

The [demonstration video](https://drive.google.com/file/d/1m5DuoPHrOL2D1xbw7a2gBtiSbTjlrpa1/view?usp=sharing)
shows the product workflow.

## Inspect a review

Open a completed report and review its summary, format-specific judgments, and
revision recommendations. Use source references to inspect the corresponding
media and time positions.

The demonstration includes a completed Coca-Cola creative review. Starting from
a completed example lets reviewers inspect the report directly.

## Compare creatives with pulse

Select multiple creatives in the library and choose **Ask Pulse**. Ask:

> Which creative communicates the product benefit most clearly, and why?
> Cite the supporting evidence.

Follow up with:

> What should we change in the second creative? Cite the supporting evidence.

Inspect the answer alongside its referenced creatives and source locations.

## Explore a campaign

Open the campaign content view to explore themes, related terms, and the
creatives behind them. Move between the collection view and individual reports
to inspect the original material.

## Local scaffold

The repository's `app.py` is an HTTP scaffold. Its default review route returns
501 and no analysis output. The hosted prototype is the product evaluation
entry; local service checks cover only the public scaffold.
