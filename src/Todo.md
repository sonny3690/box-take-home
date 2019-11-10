## TODO:

1. Winning mechansim *done*
2. Capture & Drop Mechanism
    a. Two things are interlinked.
    b. Should do capture before drop *done*
    
Capture seems to be done. Some logics need to be covered nonetheless, including
    1) p cannot be dropped into promotion zone *done*
    2) p cannot dropped into same column where there's another p *done*
    3) p can't be dropped where it would cause a checkmate

3. Check Mechanism
    1) do this last

4. Promotions
    a. essentially the same thing, except move changes *done*

5. Parse test cases & files
    a. Good to do before things start building up
    
    1. load initial positions
    2. load captured pieces
    3. load in moves

6. Extra edge cases
    a. pieces jumping