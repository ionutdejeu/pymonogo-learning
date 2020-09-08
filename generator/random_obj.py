import random
import uuid


class RandomObjGenerator:

    def get_radom_sentance(self):

        nouns = ("puppy", "car", "rabbit", "girl", "monkey")
        verbs = ("runs", "hits", "jumps", "drives", "barfs")
        adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
        adj = ("adorable", "clueless", "dirty", "odd", "stupid")
        num = random.randrange(0, 5)

        return f'{nouns[num]} {verbs[num]} {adv[num]} {adj[num]}'

    def get_random_fixed_label(self):
        i = random.randrange(0,10)
        return f'label_value_{i}'

    def get_nested_object(self):
        tags_obj = {}

        for i in range(0,20):
            tags_obj[f'tag_name_{i}'] = self.get_radom_sentance()

        obj = {
            "Paragraph": self.get_radom_sentance(),
            "number_prop": random.randrange(1458000000, 2187000000),
            "Tags": tags_obj
        }
        for i in range(0,6):
            obj[f'fixed_label_{i}'] = f'{self.get_random_fixed_label()} and {self.get_random_fixed_label()} and {self.get_random_fixed_label()}'

        return obj

    def get_set_random_obj(self,set_size:int=10):
        result = []
        for i in range(0,set_size):
            result.append(self.get_nested_object())
        return result

    def get_set_random_obj_with_id(self,set_size:int=10):
        result = []
        for i in range(0,set_size):
            result.append(self.get_nested_obj_with_id())
        return result

    def get_nested_obj_with_id(self):
        obj = self.get_nested_object()
        obj['_id'] = str(uuid.uuid1())
        return obj
