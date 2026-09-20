# 🐇 plbunny Roadmap

> *Mind the hares. Follow the tortoise. Write the story.*

plbunny is being developed in stages. The roadmap is intentionally flexible while the architecture is tested in a real writing community.

## 🐾 Phase 0 — Foundation
**Status: 🟢 In progress**
- [x] Discord application and bot
- [x] Python project structure
- [x] Slash-command support
- [x] SQLite database
- [x] Basic prompt library
- [x] `/prompt`
- [x] Per-server XP storage
- [x] `/xp`
- [x] Staff-awarded XP
- [x] `/give_xp`
- [x] GitHub repository and MIT license
- [x] Test bot in a real writing community
- [x] Broader configuration architecture
- [x] Decide initial project website structure
- [x] GitHub Pages documentation foundation

The first configuration layer is now working in the test server. Plotbunny stores server-specific settings in SQLite and exposes administrator-only configuration commands for timezone, XP, writing channel, and announcement channel.

The initial GitHub Pages site is also established as a simple static project home and roadmap. It will grow into the public documentation layer as features mature.

## 🐇 Phase 1 — Prompt System
**Status: 🔜 Next**
- [ ] Prompt library data model
- [ ] Prompt categories/tags
- [ ] Prompt archives
- [ ] Community-submitted prompts
- [ ] Prompt approval/moderation flow
- [ ] Scheduled prompts
- [ ] Per-server prompt schedules and libraries
- [ ] Prompt management commands
- [ ] Prompt history / avoid-repeat logic

## 🧁 Phase 2 — Challenge System
**Status: 🧠 Architecture/design**
- [ ] Challenge data model
- [ ] Start/end dates and configurable duration
- [ ] Daily, weekly, biweekly, and monthly cadence
- [ ] Future custom cadence
- [ ] Minimum words per entry
- [ ] Minimum total word count
- [ ] Optional maximums
- [ ] Themes, Bakeoff ingredients, and constraints
- [ ] Timezone handling
- [ ] Completion requirements
- [ ] Challenge participants and entry records
- [ ] Entry-window and missed-entry rules
- [ ] Late-entry policy
- [ ] Progress calculation
- [ ] Challenge completion and archives
- [ ] Automatic reminders
- [ ] Challenge announcement channel configuration
- [ ] Writing/submission space configuration
- [ ] Discord Forum channel support
- [ ] Regular channel/thread support
- [ ] External writing-link support
- [ ] Optional linking of Discord Forum posts to challenge entries
- [ ] Clear separation between challenge tracking and stored writing

**Design principle:** challenge duration, entry cadence, and word-count requirements remain separate settings.

**Writing-space principle:** plbunny tracks participation and progress; it does not need to store the actual prose. Writers should be able to keep their work in a Discord Forum, thread, journal, forum, personal site, or other writing platform.

A typical challenge setup may recommend:

> 📢 **Announcement channel** — challenge information, rules, deadlines, and reminders  
> ✍️ **Writing space** — preferably a Forum channel for participant entries, but other spaces can be used

The recommendation is not a requirement. The goal is to support the way writing communities already organize and archive text.

## 🐢 Phase 3 — Writing Sprints
**Status: 📋 Planned**
- [ ] Sprint data model
- [ ] Start/end timer
- [ ] Individual sprints
- [ ] Group sprints
- [ ] Sprint participation
- [ ] Optional starting/ending word counts
- [ ] Word-count progress
- [ ] Sprint history and statistics
- [ ] Optional streak tracking
- [ ] Tortoise-themed sprint messaging

Sprints should encourage **steady progress**, not turn writing into a race.

## 📚 Phase 4 — Projects
**Status: 📋 Planned**
- [ ] Project data model
- [ ] Create/edit/archive projects
- [ ] Project status
- [ ] Project word counts
- [ ] Project goals and deadlines
- [ ] Progress summaries
- [ ] Multiple projects per writer
- [ ] Optional sprint/challenge integration
- [ ] Links to external project homes

## 🎯 Phase 5 — Goals
**Status: 📋 Planned**
- [ ] Personal writing goals
- [ ] Project-specific goals
- [ ] Word-count and time-based goals
- [ ] Deadline tracking
- [ ] Progress summaries
- [ ] Goal completion
- [ ] Optional reminders

## 🏆 Phase 6 — XP, Awards & Community Progression
**Status: 🟡 Prototype exists**
- [x] Per-server XP
- [x] XP storage
- [x] Staff-awarded XP
- [ ] Automatic XP events
- [ ] XP rules/configuration
- [ ] XP history
- [ ] Awards/achievements
- [ ] Award criteria and history
- [ ] Optional Discord role integration
- [ ] Progress/leaderboard commands
- [ ] Server-specific progression settings

**Design principle:** XP measures progression; awards represent specific achievements or recognition.

## 🗓️ Phase 7 — Events & Community Tools
**Status: 📋 Planned**
- [ ] Writing events
- [ ] Scheduled write-ins
- [ ] Event reminders
- [ ] Event participation
- [ ] Community milestones
- [ ] Server-wide goals
- [ ] Utility commands

## 🛠️ Phase 8 — Server Configuration
**Status: 🟡 Foundation implemented**
- [x] Server configuration model
- [x] Configurable writing/submission spaces
- [x] Configurable announcement channel
- [x] Configurable timezone
- [x] Configurable XP enable/disable
- [ ] Configurable channels and roles
- [ ] Configurable schedules
- [ ] Configurable XP rules
- [ ] Configurable challenge defaults
- [x] Permission-aware administration
- [x] Configuration commands
- [x] Safe defaults
- [ ] Configuration documentation

The initial configuration architecture is deliberately small. It establishes the per-server persistence and administration patterns that later features can build on without hard-coding a particular community's setup.

## 🌐 Phase 9 — Project Website & Documentation
**Status: 🟡 Foundation implemented**
- [x] GitHub Pages site
- [x] Initial static project homepage
- [x] Roadmap/project status
- [ ] Feature overview
- [ ] Getting started guide
- [ ] Bot installation documentation
- [ ] Self-hosting documentation
- [ ] Configuration reference
- [ ] Challenge and sprint guides
- [ ] FAQ
- [ ] Contribution guide
- [ ] License information
- [ ] Clear distinction between self-hosted and future hosted options

**Website principle:** GitHub Pages should be the public documentation/home layer, while the GitHub repository remains the source-code and project-management home.

The first version does not need a complicated framework. A simple static documentation site is enough to start.

## 🏠 Phase 10 — Public Release, Self-Hosting & Sustainability
**Status: ⏳ Future**
- [ ] Installation documentation
- [ ] Self-hosting guide
- [ ] Environment/configuration documentation
- [ ] Database setup and migration documentation
- [ ] Upgrade/migration strategy
- [ ] Backup strategy
- [ ] Docker support
- [ ] Contribution guidelines
- [ ] Issue templates
- [ ] Security review
- [ ] Public installation flow
- [ ] Release process
- [ ] Public beta
- [ ] Evaluate optional official hosted service
- [ ] Define hosted-service boundaries
- [ ] Define sustainable pricing if a hosted service is offered
- [ ] Document any hosted-only conveniences or premium features

**Sustainability principle:** self-hosting should remain a viable free/open-source path. A future hosted service would exist for convenience and to help fund infrastructure and development, not because the underlying software requires a subscription.

## 🌱 Ideas for Later

These are deliberately **not commitments**.
- [ ] Custom challenge types
- [ ] More advanced statistics
- [ ] Server-wide writing events
- [ ] Optional competitive leaderboards
- [ ] More award types
- [ ] Import/export tools
- [ ] Additional storage backends
- [ ] Web-based administration
- [ ] Integrations with other writing tools and publishing platforms
- [ ] Additional languages/localization
- [ ] Hosted-service-only conveniences, if a hosted service is eventually offered

## 🐢 Guiding Principle

plbunny is not intended to make writers write faster at all costs.

The hare is useful for inspiration.

The tortoise is useful for persistence.

Discord can be the clubhouse without having to be the bookshelf.

**The goal is to help writers keep moving while letting them keep their writing where it works best for them.**

And if Plotbunny eventually pays for its own server by feeding a few more rabbits, so much the better. 🐇
