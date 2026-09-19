# 🐇 plbunny

**A writing-community bot for Discord, inspired by plot bunnies, the tortoise and the hare, and the legacy of `fanfic_bakeoff`.**

> *Mind the hares.*

plbunny is a Discord bot for writing communities: prompts when you need an idea, a tortoise when you need to sit down and write, and tools for keeping track of the work that follows.

It is designed for **both original fiction and fanworks**.

## ✍️ What is plbunny?

plbunny is being built as a writing-community toolkit rather than just a prompt generator.

> 🐇 **The hare brings the idea.**
> 🐢 **The tortoise keeps you moving.**

A plot bunny can get you excited about a story. A writing sprint can help you actually put words on the page. Challenges and goals can give those words somewhere to go.

The long-term goal is a self-hostable alternative to the collection of writing-community tools a Discord server may otherwise rely on, including the kinds of features provided by Writer-Bot.

### Planned features

#### 🐇 Prompts
* Scheduled general writing prompts
* On-demand random prompts
* Prompt archives
* Community-submitted prompts
* Configurable prompt libraries
* Prompt categories and themes

#### 🐢 Writing
* Writing sprints
* Individual and group sprints
* Sprint timers
* Word-count tracking
* Writing streaks and progress

#### 🧁 Challenges
* Bakeoff-style writing challenges
* Daily, weekly, biweekly, monthly, and configurable cadences
* Configurable challenge duration
* Per-entry and total word-count requirements
* Themes, ingredients, constraints, and other rules
* Challenge opening and closing dates
* Automatic reminders
* Participant progress and entry tracking
* Dedicated challenge announcement channels
* Writing/submission spaces, including Discord Forums
* Links to writing hosted elsewhere

#### 📚 Projects & Goals
* Writing project tracking
* Project word counts
* Personal and project-specific goals
* Progress tracking
* Deadlines

#### 🏆 Community & Progression
* Automatic XP
* Staff-awarded XP
* Awards and achievements separate from XP
* Optional Discord role integration
* Community events
* Server-level configuration

## 📝 Discord is the clubhouse, not necessarily the bookshelf

Discord is useful for the **community layer** of a writing group: conversation, prompts, sprints, announcements, reminders, celebrations, and finding people to write with.

But Discord's fast-moving chat model is not always the best place to keep actual writing.

Writing communities have long used **forums and journals** for text submissions because they give each piece of work a persistent home. A submission can have its own title, discussion, replies, and history instead of disappearing into a busy chat channel.

That is why plbunny is designed around a distinction between **community tools** and **writing spaces**.

A challenge might use:

* 📢 a Discord channel for announcements and reminders
* ✍️ a Discord Forum channel for participant entries
* 💬 a regular channel or thread for discussion
* 📖 a forum or journal elsewhere
* 🌐 a personal website or writing platform
* 🔗 another external archive or publishing site

plbunny does not need to own the writing itself. Instead, it can track the participation that matters to a challenge:

> **Ceri → October Daily Drabbles → Day 7 → 183 words → link to the entry**

This keeps the bot focused on prompts, challenges, schedules, progress, goals, and community features while letting writers keep their actual work wherever it works best for them.

**Your writing has a home. Plotbunny helps run the writing community around it.**

## 🧁 Inspired by the old internet

### Plot bunnies

A **plot bunny** is a story idea that appears out of nowhere, demands to be written, and frequently reproduces while you're trying to work on something else.

Sometimes you catch one.

Sometimes the hares get away from you.

### The tortoise and the hare

The hare is excellent at generating momentum. The tortoise is excellent at actually getting there.

Writing is rarely helped by treating every project like a race. plbunny's sprint system is built around **making time to write and making steady progress**, rather than treating word count as a competition.

> **Mind the hares. Follow the tortoise. Write the story.**

### `fanfic_bakeoff`

The challenge system takes inspiration from the old **`fanfic_bakeoff`** community tradition: give writers ingredients, constraints, or prompts and see what they bake.

plbunny carries that idea beyond fandom. **Original fiction and fanworks are equally welcome.**

## 🏠 Free to self-host, with hosted options possible later

plbunny is intended to remain **free and open source for communities that want to run it themselves**.

Self-hosting means a community can run its own instance with its own Discord application, bot token, prompt library, schedules, server configuration, and database.

In the future, the project may also offer an **optional hosted service** for communities that would rather not maintain their own bot infrastructure. A hosted service could help cover hosting, backups, maintenance, and development costs while leaving self-hosting available.

The goal is not to put the core writing-community toolkit behind a paywall.

> **The software can be free. The rabbit still has to eat.**

Any hosted service, pricing, and premium features will be documented separately when they actually exist. They are not part of the current early-development release.

## 🌐 The Plotbunny website

The project website and documentation are planned to live on **GitHub Pages**, alongside the source repository.

The website will provide a public home for:

* 📖 User documentation
* 🐇 Feature guides
* 🧁 Challenge documentation
* 🐢 Sprint documentation
* 🏠 Self-hosting instructions
* 💻 Installation and configuration guides
* 🗺️ Roadmap and project status
* 🤝 Contribution information
* 📜 Licensing information
* 🌱 Future hosted-service information, if offered

Keeping the documentation with the code means the project can maintain **one source of truth** rather than maintaining a separate website and repository.

## 🚧 Project Status

**Current status: Early development**

plbunny is currently being developed and tested within a small writing community. The repository is public, but the bot is **not yet ready for general installation**.

The current focus is establishing the underlying data model and core writing-community systems before expanding into more complex automation.

See [`ROADMAP.md`](ROADMAP.md) for the current development plan.

## 🛠️ Planned Technology

* **Python**
* **discord.py**
* **SQLite**
* **Discord Application Commands / Slash Commands**

The project is being designed so individual Discord servers can configure their own schedules, channels, prompt libraries, challenges, and writing activities without changing the bot's source code.

## 🤝 Contributing

Contributions will be welcome once the project reaches public release. Potential contributions include code, bug reports, feature requests, documentation, prompt ideas, challenge formats, translations, and testing.

## 📜 License

plbunny's source code is released under the **MIT License**. See [`LICENSE`](LICENSE) for the full license text.

The source-code license does not automatically grant permission to reproduce or redistribute creative writing, prompts, or other content included with a particular installation.

## 🐇 Why "plbunny"?

Because sometimes you sit down intending to write one story.

Then another idea appears.

And another.

And suddenly there are seventeen tabs open, three unfinished documents, two worldbuilding notebooks, and a suspiciously detailed history for a character who was supposed to have one line.

The plot bunnies are multiplying.

**Mind the hares.**
