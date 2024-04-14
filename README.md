# TrekTician

## Inspiration
Traveling is rewarding; however, planning can be stressful. Many plans their trip with a travel agency due to convenience, while others choose to plan online because of flexibility. TrekTician gives a one-stop tour planner that generates all aspects of your travel plan tailored to your preferences, which provides BOTH convenience and flexibility.

## What it does

Currently, the user can select which country they would like to travel to, or if they are seeking a surprise, they can select the button that says, "I'm feeling lucky". Then, upon selecting the country they want to visit, then a list of cities will be generated as suggested from the GEMINI API and the screen will display various cities while also listing a description and image of the city. 

Upon providing the user preferences, we provide a full itinerary, including daily activities, the most suitable hotel based on the activities, and a budget for the trip. Please note the following steps have been completed in the back-end but not yet implemented in the front-end. See the Jupyter notebooks for how the back-end is implemented. 

1. By picking a country and a travel style, we will introduce you to cities worth visiting based on your preferences. 
2. Then, we will provide you with a list of popular tourist attractions and restaurants for you to add your MUST VISIT list. 
3. Based on your MUST VISIT list, travel and hotel preferences, we will generate an itinerary tailored to you, which includes all of your travel bucket list items. The itinerary includes daily activities, the most suitable hotel based on your daily activities, and a budget for the trip.

## How we built it
We built it with a variety of front and back end technologies that we learned in just the span of a few days during the hackathon. For the front end, we primarily used Vite and React. For the back end, we use Flask and python. We used the python requests library to make GEMINI API calls and to retrieve images of the cities from the Google custom search engine API. 

## Challenges we ran into
One of the hardest parts of our project was integrating the frontend and backend. Most of our team had never used React, Flask, or GEMINI before, so learning both front end and back end software while integrating the two parts was an extremely tricky process. 
Since the python SDK version of GEMINI did not offer the capability to format the responses in JSON, we resorted to using a python requests library to call the GEMINI API through cURL for JSON formatted responses. Although this was a bit slower, this guaranteed that the responses made by GEMINI were formatted into proper JSON, which is the format we used to transfer information from the back end to the front end. 

Because it was also some of our first times’ using React, learning to work with components and other frameworks was difficult. Our first big hurdle was definitely integrating the globe on our front page using react-globe.gl, but it was the first step into quickly learning the technology. We learned a lot about React through trying to implement such a tricky component, but ultimately we successfully implemented it into our website. 

## Accomplishments that we're proud of
We’re proud of how we were able to make significant progress during the past two days. We efficiently split up our team into two groups: each focusing on either frontend or backend. By splitting up the work and being able to focus on the core functionality of both the UI as well as the AI integration. 
All but every member of the team had no prior experience working with frontend or backend based on the assignment they were working with and so we learned to bootstrap everything in just a few days of coding. 

## What we learned
We learned a lot in the span of a few days. On the front end, we learned how to use React and Vite to create an amazing frontend. On the back end, we learned how to use the GEMINI API. For instance, we learned how to specify the output to be strictly JSON, which made communication between the front end and back end of the project much simpler. We also leveraged the custom engine search API provided by Google to get URLs to images of the particular city that the user would like to visit. 

## What's next for TrekTician
We will further develop our front end design to match our backend.
In the future, we also wish to provide additional features, such as allowing the user to change items within the final itinerary, providing additional hotel and plane options, and linking users to booking sites will be the next steps of making TrekTician more convenient and flexible.  
