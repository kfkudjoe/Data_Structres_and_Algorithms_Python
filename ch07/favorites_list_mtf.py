from favorites_list import FavoritesList
from positional_list import PositionalList



class FavoritesListMTF(FavoritesList):
    """
    List of elements ordered with move-to-front heuristics.
    """

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        # Move  accessed item at Position p to front of the list
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))      # delete/reinsert

    # override top because list is no longer sorted
    def top(self, k):
        # Generate sequence of top k elements in terms of access count
        if not 1 <=  k <=  len(self):
            raise ValueError("Illegal value for k")

        # Make a copy of the original list
        temp = PositionalList()

        for item  in  self._data:       # positional lists support iteration
            temp.add_last(item)

        # We repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find an report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)

            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk =  temp.after(walk)

            # we have found the element with the highest count
            yield highPos.element().value   # report element to user
            temp.delete(highPos)        # remove from temp list



if __name__ ==  "__main__":
    fav = FavoritesListMTF()

    for c in "Hello. this is a test of mtf":
        fav.access(c)

        k = min(5, len(fav))

        print("Top {0}) {1:25} {2}".format(k, [x for x in fav.top(k)], fav))