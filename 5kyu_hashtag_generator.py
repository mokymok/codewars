def generate_hashtag(s):
    if s=='' or len(s)>140:return 0
    else:return f'#{s.title().replace(" ","")}'
