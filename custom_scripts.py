def get_slug(validated_data):
        sub_name = validated_data['name']
        sub_name = sub_name.replace(',', '')
        slug = sub_name.replace(' ', '-')
        return slug.lower()