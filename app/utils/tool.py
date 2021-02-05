class Tool:
    def to_list_all(self, comments):
        t_list = []
        for comment in comments:
            t_list.append(dict(comment))
        return t_list

    def to_dict_all(self, comments):
        t_dict = {}
        for comment in comments:

            if comment['id'] in t_dict:
                t_dict[comment['id']]['data'].append(dict(comment))
            else:
                t_dict[comment['id']] = {'id': comment['id'], 'sutName': comment['sutName'],
                                         'itcode': comment['itcode'], 'backgroud_type': comment['backgroud_type'],
                                         'data': [dict(comment)]}

        print(len(t_dict))
        return list(t_dict.values())
        # return t_dict
