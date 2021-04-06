# LEAGUE WIKIA

This project aims to show a few couple things.

First is *Object Oriented Data Analysis*. The primary interface used in the analyses are Jupyter Notebooks (e.g. `Thresh.ipynb`). Behind these notebooks is the `Champions` module where classes like `ChampionAbility` and `ChampionWikia` encapsulate reusable code that couple state and behavior together.

`ChampionWikia` is a class representing a specific League of Legends champion.

`ChampionAbility` is a `dataclass` that hold together some key information about a champions skill or ability.

I have also included some basic tests in this project via `pytest`.

Lastly, I tried to use the Jupyter Notebook for VSCode in this project.

Some quick wins:
- Dark mode
- Auto-completion
- Verbose cells
- Export as HTML
- Most used shortcut (Alt+Enter) has the same functionality.
- Ease of work between modules and notebooks.

Quite a few nitpicks
- Kernel, virtual environments, everything has to be set up again.