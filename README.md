# Movie Recommendation System

Given an input movie, this program will recommend five movies to you based on your movie's plot, cast, and director.

Specifically, the program finds movies with the highest cosine similarity for Term Frequency Inverse Document Frequency for a bag of words including the plot synopsis, director, and cast members.

### Getting Started

Download the raw data [from Kaggle](https://www.kaggle.com/jrobischon/wikipedia-movie-plots).

In the command line, run `python recommend_movie.py <<Movie Title>>`

**The Anchorman: The Legend of Ron Burgundy**
```
Rank: 1
Title: Anchorman 2: The Legend Continues
Movie Similarity Score: 15.9,
Cast: Will Ferrell, Christina Applegate, Paul Rudd, David Koechner, Steve Carell, Kristen Wiig, James Marsden, Dylan Baker, Meagan Good, Harrison Ford, Greg Kinnear, Josh Lawson, Vince Vaughn, Luke Wilson, Nicole Kidman, Fred Willard, Chris Parnell, Fred Armisen, Jim Carrey, Sacha Baron Cohen, Drake, Kirsten Dunst, Tina Fey, Will Smith, Liam Neeson, Amy Poehler, John C. Reilly, Kanye West, Billie Joe Armstrong, Mike Dirnt, Trey Cool, Jason White, Lewis Hamilton
Director: Adam McKay
Year: 2013

Rank: 2
Title: The Other Guys
Movie Similarity Score: 10.0
Cast: Samuel L. Jackson, Mark Wahlberg, Will Ferrell, Dwayne Johnson, Eva Mendes, Anne Heche, Michael Keaton, Steve Coogan, Ray Stevenson
Director: Adam McKay
Year: 2010

Rank: 3
Title: Talladega Nights: The Ballad of Ricky Bobby
Movie Similarity Score: 10.0
Cast: Will Ferrell, John C. Reilly, Sacha Baron Cohen
Director: Adam McKay
Year: 2006

Rank: 4,
Title: Step Brothers,
Movie Similarity Score: 9.4,
Cast: Will Ferrell, John C. Reilly, Richard Jenkins, Mary Steenburgen, Adam Scott, Kathryn Hahn,
Director: Adam McKay
Year: 2008

Rank: 5
Title: All That Heaven Allows
Movie Similarity Score: 8.1
Cast: Jane Wyman, Rock Hudson
Director: Douglas Sirk
Year: 1955
```

**Training Day**

```
Rank: 1
Title: The Unknown
Movie Similarity Score: 11.0
Cast: Lon Chaney, Joan Crawford
Director: Tod Browning
Year: 1927

Rank: 2
Title: "Brooklyns Finest"
Movie Similarity Score: 11.0
Cast: Richard Gere, Don Cheadle, Ethan Hawke, Wesley Snipes
Director: Antoine Fuqua
Year: 2010

Rank: 3
Title: The Magnificent Seven
Movie Similarity Score: 10.7
Cast: Denzel Washington, Chris Pratt
Director: Antoine Fuqua
Year: 2016

Rank: 4
Title: The Equalizer
Movie Similarity Score: 9.6
Cast: Denzel Washington, Marton Csokas, Chloe Grace Moretz, Bill Pullman
Director: Antoine Fuqua
Year: 2014

Rank: 5,
Title: Tears of the Sun
Movie Similarity Score: 8.2
Cast: Bruce Willis, Monica Bellucci, Cole Hauser
Director: Antoine Fuqua
Year: 2003
```
