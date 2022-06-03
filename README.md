# Bayan 1.0
<div dir="rtl">
سلام . bayan یک کتابخونه برای جمع آوری اطلاعات از وبلاگ های بیان در پایتون هستش. کار با این کتابخونه بسیار ساده هستش چون اولا خیلی حجیم نیست دوما اسامی توابع کاملا واضح انتخاب شدن . 



# Weblog Class

<div dir="rtl">
برای جمع آوری اطلاعات در مورد وبلاگ مورد نظر (مثلا ho55ein.blog.ir) . ابتدا یک شیء از کلاس Weblog میسازیم :

‍‍```>>> import bayan```
```>>> weblog = bayan.Weblog("https://ho55ein.blog.ir")```

<div dir="rtl">
حالا خیلی راحت میتونیم از توابع زیر استفاده کنیم : 

# getInfo()
<div dir="rtl">
این تابع یک سری اطلاعات کلی در مورد وبلاگ مثل (عنوان وبلاگ ، تعداد دنبال کنندگان ، تعداد کامنت ها ، تعداد پست ها و...) را در قالب یک لیست بر میگرداند . البته ممکن است در بعضی از وبلاگ ها با توجه به تنظیماتی که صاحب وبلاگ اعمال کرده ، برخی از این اطلاعات در دسترس نباشد بنابراین تابع فقط اطلاعاتی که در دسترس هست رو بر میگردونه .

```>>> weblog.getInfo()```
```{'TITLE': 'حسین نوشته ها ...', 'POSTS_COUNT': 114, 'COMMENTS_COUNT': 385}```
```>>>```

# getPages()
<div dir="rtl">
این تابع لیستی از صفحات مستقل وبلاگ مورد نظر رو بر میگردونه.

```>>> weblog.getPages()```
```[{'TITLE': 'علاقه مندی ها', 'LINK': 'https://ho55ein.blog.ir/page/who-is-hossein'}, {'TITLE': 'تماس با me :)', 'LINK': 'https://ho55ein.blog.ir/page/message-to-hossein'}, {'TITLE': 'My Playlist', 'LINK': 'https://ho55ein.blog.ir/page/My-Playlist'}]```
```>>>```

# getLinks()
<div dir="rtl">
این تابع لیستی از پیوند های وبلاگ مورد نظر رو بر میگردونه .

```>>> weblog.getLinks()```
```[{'TITLE': 'Mr Python (Hacking With Python)', 'LINK': 'https://mrpython.blog.ir'}, {'TITLE': 'OG150 Hacking Tutorials', 'LINK': 'http://www.og150.com/tutorials.php'}]```
```>>>```

# getLastPosts()
<div dir="rtl">
این تابع لیستی از آخرین پست های وبلاگ مورد نظر رو برمیگردونه . 

# getLastFollowers()
<div dir="rtl">
همانطور که میدونید در وبلاگ هایی که جعبه ی دنبال کنندگان نمایش داده میشه ، لیستی از آخرین دنبال کننده ها وجود داره . این تابع در صورت وجود باکس دنبال کنندگان لیستی از آخرین دنبال کنندگان وبلاگ مورد نظر را برمیگرداند.

# bayan.getChanges()
<div dir="rtl">
این تابع لیست وبلاگ های بروز شده رو بر میگردونه .

<div dir="rtl"><br><br>
همچنین هر شیء از کلاس Weblog دارای یک متغییر یا ویژگی به نام follow_link است که لینک دنبال کردن وبلاگ مورد نظر را در خود نگه میدارد :

```>>> print(weblog.follow_link)```
```http://blog.ir/panel/-/followed_blogs?follow=https://ho55ein.blog.ir```
```>>>```





‍



