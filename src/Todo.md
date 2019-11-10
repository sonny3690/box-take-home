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
    1) do this last.

    Parts to address:

    1) Detecting check through going through all of opponents coordinates & pieces
    2) Finding available moves
        a. Do this through check mechanism on all valid moves of king
            -check mechanism: param: coord to reach, player pieces
        b. If distance is greater than 1, trace out blocking paths, including capturing the piece itself.
        Remember that piece can't be captured
            Find all pieces that contain coordinate as valid
            -In order for block to happen, I need to address issue of jumping

    TODO:
    
    - create driveLocation(playerType) -> returns tuple containing drive location *done*
    - Address jumping *done*
    - Given two coordinates, _inbetweenpath *done*
    - Create reachable function: pieceCanReach(piece, coord) in board -> returns True or False *done*
    - Create allReachables: allReachables(player, coord) in board -> returns list of pieces of player
        - At each turn, we check driveLocation with allReachables of the opposite player, and engage with check that way *done*
        - Show available moves through checking allReachables for each valid move drive has *done*
            - Check if checker is reachable by other player *done*
            - Check if inbetweenpath is reachable by other player *done*
                - Need to check if moving piece would cause check *flaw in code, but might not be covered by testcase*
            - If not, we decalre a check mate *done*

    - Use reachable function to address check
    

4. Promotions
    a. essentially the same thing, except move changes *done*

5. Parse test cases & files
    a. Good to do before things start building up
    
    1. load initial positions *done*
    2. load captured pieces *done*
    3. load in moves *done*

6. Extra edge cases
    a. pieces jumping
    


## Test Cases

basicCheck.in				moveOutOfCheck.out
basicCheck.out				movingIntoCheck.in
blockOutOfCheck.in			movingIntoCheck.out
blockOutOfCheck.out			notesIllegalMove.in
capture.in				notesIllegalMove.out
capture.out				notesMoves.in
captureAndPromote.in			notesMoves.out
captureAndPromote.out			notesPromotion.in
captureDrop.in				notesPromotion.out
captureDrop.out				occupiedDrop.in
captureOutOfCheck.in			occupiedDrop.out
captureOutOfCheck.out			previewIllegalMove.in
checkmate.in				previewIllegalMove.out
checkmate.out				previewPromotion.in
doubleCheck.in				previewPromotion.out
doubleCheck.out				promoteLeavingZone.in
doublePreviewDrop.in			promoteLeavingZone.out
doublePreviewDrop.out			promoteWithinZone.in
driveIllegalMove.in			promoteWithinZone.out
driveIllegalMove.out			promotedCaptureDrop.in
driveMoves.in				promotedCaptureDrop.out
driveMoves.out				promotedGovernanceIllegalMove.in
drivePromotion.in			promotedGovernanceIllegalMove.out
drivePromotion.out			promotedGovernanceMoves.in
drop.in					promotedGovernanceMoves.out
drop.out				promotedNotesIllegalMove.in
dropEmptyHand.in			promotedNotesIllegalMove.out
dropEmptyHand.out			promotedNotesMoves.in
dropOpponentsPiece.in			promotedNotesMoves.out
dropOpponentsPiece.out			promotedPreviewIllegalMove.in
dropOutOfCheck.in			promotedPreviewIllegalMove.out
dropOutOfCheck.out			promotedPreviewMoves.in
dropWrongPiece.in			promotedPreviewMoves.out
dropWrongPiece.out			promotedRelayIllegalMove.in
forcedPreviewPromotion.in		promotedRelayIllegalMove.out
forcedPreviewPromotion.out		promotedRelayMoves.in
governanceIllegalMove.in		promotedRelayMoves.out
governanceIllegalMove.out		promotedRelayPromotion.in
governanceMoves.in			promotedRelayPromotion.out
governanceMoves.out			relayIllegalMove.in
governancePromotion.in			relayIllegalMove.out
governancePromotion.out			relayMoves.in
immediatePreviewDropMate.in		relayMoves.out
immediatePreviewDropMate.out		relayPromotion.in
initialMove.in				relayPromotion.out
initialMove.out				shieldIllegalMove.in
initialResponse.in			shieldIllegalMove.out
initialResponse.out			shieldMoves.in
loseOnLastMove.in			shieldMoves.out
loseOnLastMove.out			shieldPromotion.in
lowerIllegalPromotion.in		shieldPromotion.out
lowerIllegalPromotion.out		tieGame.in
lowerStuckPreviewDrop.in		tieGame.out
lowerStuckPreviewDrop.out		upperIllegalPromotion.in
manyWaysOutOfCheck.in			upperIllegalPromotion.out
manyWaysOutOfCheck.out			upperStuckPreviewDrop.in
mateWithDrop.in				upperStuckPreviewDrop.out
mateWithDrop.out			winOnLastMove.in
moveOutOfCheck.in			winOnLastMove.out