def read_misc_file(filepath) -> str:
    with open(filepath) as my_file:
        file_content = my_file.read()
    return file_content


def bread_file_to_list(filepath) -> list:
    with open(filepath) as my_file:
        bread_list = [s.strip() for s in my_file.readlines()]
    return bread_list


misc = ['update_log', 'help', 'faq']
misc_paths = ['text_files/misc_text_files/updateLog.txt', 'text_files/misc_text_files/help.txt',
              'text_files/misc_text_files/faq.txt']
misc_to_content = {misc: read_misc_file(path) for misc, path in zip(misc, misc_paths)}
updateLog, helpContent, faqContent = misc_to_content.values()

breads = ['common', 'rare', 'mythical', 'legendary']
bread_paths = ['text_files/bread_data/common_bread.txt', 'text_files/bread_data/rare_bread.txt',
               'text_files/bread_data/mythical_bread.txt', 'text_files/bread_data/legendary_bread.txt']
bread_to_list = {bread: bread_file_to_list(path) for bread, path in zip(breads, bread_paths)}
common_bread, rare_bread, mythical_bread, legendary_bread = bread_to_list.values()

pantry_limit = 1000
bake_cooldown = 600
