from aiogram import types

media = types.MediaGroup()
media.attach_photo(types.InputFile('./banners1.jpg'),
                   'Подборка шапок, сделанных мной для различных проектов🔥')
media.attach_photo(types.InputFile('./banners2.jpg'),
                   'Подборка шапок, сделанных мной для различных проектов🔥 (2)')
media.attach_photo(types.InputFile('./logos.jpg'),
                   'Подборка логотипов сделанных мной (Здесь только те, что были сделаны недавно🔥)')
media.attach_photo(types.InputFile('./prewievs.jpg'),
                   'Последние работы, сделанные мной для различных ютуберов🔥')