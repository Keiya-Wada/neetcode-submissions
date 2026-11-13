class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for word in strs:
                to_append = "".join(sorted(word))
                my_dict[to_append].append(word)
        return list(my_dict.values())


        