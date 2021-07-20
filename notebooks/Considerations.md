Possible factors affecting alert forecast on traffic:
- Schedule of public transport. Variation on schedule for festivities.
- Rush hours.
- Festivities/Events.
- Weather conditions.
- Terrorist Alert / Police Activity.
- Emergencies.

EDA STATISCS:

Notifications.json

2-Christian
1-Tim
3/4-Edu

1. Drop date -2
2. Convert date timestamp -2
3. Relate users and notification opened with a rate (0 if they never opened a not, 1 if they open all) -1
4. Observe how long do they take to react (open or dismissing) -2
5. Get maybe a user target / cluster them. -3    (Reaction time (after incident happens, until they open or dismiss) vs Open/Dismissed (while the incident is still active)).
6. Try to identify which agencies are considered by the users as useless, regarding notification dismissing. If we find that some agencies are always dismissed, maybe we can ignore them so we don't sent notification that give no value. -3 (Not priority)
7. Query the people
8. Divide which incidents are already expired when users do an action with the notification. Analyze that to offer users a summary of the day at night/morning. -3

Alerts.json

1. Function to ignore the notifications dismissed who were already closed. -4
2. Plot a heatmap on a map for the opening rate using the coordinates - 1
3. Make a function to relate cause, effect,agency, and message with the opening rate. -4

Project Solving approaches

P1: Tone of voice

1. Apply a model for name entity recognition, so we get the names of streets, road, cities, and services that should not be changed.
2. Apply a model that generates text variations with the same content.
3. Apply A/B Test.
4. Learn from it, reapply.

! Idea: Add a library to calculate distances between coordinates. Add a function that add to messages the names of POI when they are nearby. Tim get your hands on Openstreetmap!

Metric: Ratio of opening

P2: Traffic light system of alerts:

1. Model for regression. Target: Opening ratio. Features: Cause, effect, agency, (text) , location.
2. Base model: Decision tree. Next model: Ensemble of random forest, ...,....
Metric: RMSE. 67% accuracy as goal.

OUTPUT Metric: Scale of importance (matrix of weight between cause, effect, agency, message,location)


P3: Alert forecasting

#Remember the story of Paco the farmer ("00205").
BULLET IDEA: Stack users on a chat for the incident follow-up.


QUESTIONS FOR ELLEN

1. Regarding data cleaning, around 28000 rows could not be linked (alerts with notifications).
2. Could we get the name of the agencies for each code?
3. Problems with the app.

https://www.google.de/search?q=plotting+time+series+density+plot&tbm=isch&ved=2ahUKEwiYtq_3tO_xAhUUSOUKHZoOCRQQ2-cCegQIABAA&oq=plotting+time+series+density+plot&gs_lcp=CgNpbWcQAzoECAAQEzoGCAAQHhATULEnWMtHYPVIaANwAHgAgAFAiAGYB5IBAjE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=ZpX1YJjrIJSQlQeanaSgAQ&bih=679&biw=1314