from typing import List


class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        known = dict()
        inits = expeditions[0].split('->')
        for init in inits:
            known[init] = 1
        most_trip = -1
        most_found = 0
        for trip in range(1, expeditions.__len__()):
            new_get = expeditions[trip].split('->')
            this_found = 0
            for get in new_get:
                if get:
                    try:
                        known[get] += 1
                    except KeyError:
                        this_found += 1
                        known[get] = 1
            if this_found > most_found:
                most_trip = trip
                most_found = this_found
        return most_trip


print(Solution().adventureCamp(expeditions=["leet->code", "leet->code->Campsite->Leet", "leet->code->leet->courier"]))
print(Solution().adventureCamp(expeditions=["Alice->Dex", "", "Dex"]))
print(
    Solution().adventureCamp(expeditions=["", "Gryffindor->Slytherin->Gryffindor", "Hogwarts->Hufflepuff->Ravenclaw"]))
