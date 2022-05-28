from scipy.ndimage import find_objects, label


def validate_battlefield(field):
    # write your magic here
    labeled, ncomponents = label(field)
    # check overlap or be in contact
    for row in range(len(labeled)):
        for col in range(len(labeled[0])):
            # check every neighbour cell for current cell
            if labeled[row][col] != 0 and 0 < row < 9 and 0 < col < 9:
                if labeled[row][col-1] in [0, labeled[row][col]] and labeled[row][col+1] in [0, labeled[row][col]] and labeled[row-1][col] in [0, labeled[row][col]] and labeled[row+1][col] in [0, labeled[row][col]] \
                    and labeled[row-1][col-1] in [0, labeled[row][col]] and labeled[row-1][col+1] in [0, labeled[row][col]] \
                        and labeled[row+1][col-1] in [0, labeled[row][col]] and labeled[row+1][col+1] in [0, labeled[row][col]]:
                    pass
                else:
                    return False
    ships = 0
    cruisers = 0
    destroyers = 0
    submarines = 0
    for obj in find_objects(labeled):
        if labeled[obj].shape in [(1, 4), (4, 1)]:
            ships += 1
        elif labeled[obj].shape in [(1, 3), (3, 1)]:
            cruisers += 1
        elif labeled[obj].shape in [(1, 2), (2, 1)]:
            destroyers += 1
        elif labeled[obj].shape == (1, 1):
            submarines += 1
    return (ships == 1 and cruisers == 2 and destroyers == 3 and submarines == 4)
