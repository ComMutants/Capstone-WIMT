Possible factors affecting alert forecast on traffic:
- Schedule of public transport. Variation on schedule for festivities.
- Rush hours.
- Festivities/Events.
- Weather conditions.
- Terrorist Alert / Police Activity.
- Emergencies.

EDA STATISCS:

Notifications.json

1. Drop date
2. Convert date timestamp
3. Relate users and notification opened with a rate (0 if they never opened a not, 1 if they open all)
4. Observe how long do they take to react (open or dismissing)
5. Get maybe a user target / cluster them.
6. Try to identify which agencies are considered by the users as useless, regarding notification dismissing. If we find that some agencies are always dismissed, maybe we can ignore them so we dont sent notification that give no value.

Alerts.json

1. Function to ignore the notifications dismissed who were already closed.
2. Plot a heatmap on a map for the opening rate using the coordinates
3. Make a function to relate cause, effect,agency, and message with the opening rate.

Project Solving approaches

P1: Tone of voice

1. Apply a model for name entity recognition, so we get the names of streets, road, cities, and services that should not be changed.
2. Apply a model that generates text variations with the same content.
3. Apply A/B Test.
4. Learn from it, reapply.

! Idea: Add a library to calculate distances between coordinates. Add a function that add to messages the names of POI when they are nearby. Tim get your hands on Openstreetmap!

Metric: Ratio of opening?

P2: Traffic light system of alerts:

1. Model for regression. Target: Opening ratio. Features: Cause, effect, agency, (text) , location.
2. Base model: Decision tree. Next model: Ensemble of random forest, ...,....
Metric: RMSE

OUTPUT Metric: Scale of importance (matrix of weight between cause, effect, agency, message,location)


P3: Alert forecasting