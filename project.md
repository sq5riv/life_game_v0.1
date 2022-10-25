#Project.
##Backend
###Endpoints
0./ <br>
/ Method GET
Serves main page of project. <br>
1.Login <br>
/login Method POST
Gets username and hashed password.
Add session token to database.
Returns token. <br>
2.Logout <br> 
/login Method DELETE 
Gets token and finish session. Deletes token from database. <br>
3.Add new user <br> 
/nu Method POST Gets username, mail, hashed password. Adds new user to database. Returns Boolean. <br>
4.Add new card <br> 
/newcard Method POST Gets json with card stats. Adds card to database. Returns card ID <br>
5.Update card <br>
/card Method PUT. Gets card ID and stats. Updates card in database. Returns card ID <br>
6.Get list of cards <br>
/list Method GET. Gets conditions for cards. Returns cards stats. <br>
7.Get card <br>
/card method GET. Gets card id. Returns card stats. <br>
8.Set rules <br>
/rules method POST. Get json with rules. <br>
9.Get rules list <br>
/ruleslist method GET. Returns list of rules. <br>
8.Save game <br>
/game/save method POST. Gets game state. Save game state in database. Returns game id. <br>
9.Open game <br>
/game/open method GET. Gets game id. Returns game state. <br>
10.Get game list <br>
/game/list method GET. Return list of games from database. <br>
###Database tables
1.Users <br>
1.1 User_id
1.2 Token
1.3 Password
2.Cards <br>
2.1 Card_id
2.2 ... card stats
2.3 card image URL
3.Games <br>
3.1 Game_id
3.2 Player_id
3.3 Game_state JSON
4.Rules <br>
4.1 ID
4.2 set of rules in JSON
5.Decks <br>
5.1 Deck_id
5.2 Deck_author
6.Deck_relation_table
6.1 Deck_id
6.2 Card_id
##Frontend
1.Main page <br>
2.Card component <br>
3.New user <br>
4.Game field <br>
5.New card form <br>
6.Deck form <br>
7.Rules form<br>