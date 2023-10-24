## Unlocking Fantasy Football Success with `RosterIQ`: A Statistical Model for Crafting Your Winning Lineup

One of the more challenging aspects of managing a fantasy team is correctly the right players to start. With `RosterIQ`, we take the guesswork out of setting your fantasy line-up! `RosterIQ` is a statistical model powered by historical projections and actual player performance.

### Projected Performance vs. Actual Performance
- Factors that complicate decision making
    - Extreme weather can impact a teams decision to lean in a more run forward game plan, which can decrease the projected point total of WR and QB positions, and increase RB production 
    - Offensive and defensive schemes may be mismatched in a way that benefits or works to the detriment of your team
    - The probability of players playing through injuries
    - This is where expert consensus rankings come in! Expert Consensus Rankings provide an estimate for how  a player is expected to perform given the predictions of experts that build these esoteric factors into their decision making.

- We then build a statistical model of player performance by fitting log-Normal distributions to the historical performance of fantasy players for each position (and each tier where the tiers are decided by some statistical test to be decided later). We choose log-normal to account for the boom-ness or bust-ness of a players performance

### Correlated Player Performance

- We also model the correlations between players on the same team
