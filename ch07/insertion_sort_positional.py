def insertion_sort(posList):
    # Sort Positional List of comparable elements into increasing order.

    if len(posList) > 1:        # otherwise, no need to sort it
        marker = posList.first()

        while marker != posList.Last():
            pivot = posList.after(marker)       # next item to place
            pivotValue  = pivotValue.element()

            if pivotValue > marker.element():      # pivot is already sorted
                marker = pivot     # pivot becomes new marker
            else:       # must relocate pivot
                walk =  marker      # find leftmost item greater than value

                while (walk != posList.first()) and (posList.before(walk).element() > pivotValue):
                    walk = posList.before(walk)
                
                posList.delete(pivot)
                posList.add_before(walk, pivotValue)        # reinsert value before walk
