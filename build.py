F=False
E='GET'
D='methods'
import dill as B,webpy as C
from flask import Flask
A=Flask('app','/static','C:\\Users\\carlf\\programs\\webpy-app\\static',None,F,F,'html','C:\\Users\\carlf\\programs\\webpy-app\\instance',F,'C:\\Users\\carlf\\programs\\webpy-app')
B.loads(b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00\x8c\x03app\x94\x8c\x0bwebpy_setup\x94\x93\x94.')(A)
A.route('/',**{D:[E]})(C.appbind(lambda _:'<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<script src="../static/js/index.js" defer></script>\n\t\t<link rel="stylesheet" href="../static/css/theme.css"/>\n\t\t<link rel="stylesheet" href="../static/css/index.css"/>\n\t\t<title>Login</title>\n\t</head>\n\t<body\n\tclass="page-center"\n\tstyle="zoom: 1.5">\n\t\t<h1 id="heading">Sign In!</h1>\n\t\t<form action="login" method="post">\n\t\t\t<input \n\t\t\ttype="text" \n\t\t\tplaceholder="username"\n\t\t\tname="username"\n\t\t\trequired\n\t\t\tautofocus/>\n\n\t\t\t<br/>\n\n\t\t\t<input\n\t\t\ttype="password"\n\t\t\tplaceholder="password"\n\t\t\tname="password"\n\t\t\trequired\n\t\t\tautofocus/>\n\n\t\t\t<br/>\n\n\t\t\t<button\n\t\t\tid="login-sumbit"\n\t\t\ttype="submit"\n\t\t\tclass="btn btn-yellow"\n\t\t\tstyle="margin-top: 5px;">Login</button>\n\t\t</form>\n\t</body>\n</html>',A,'/_handler'))
A.route('/calculator/',**{D:[E]})(C.appbind(B.loads(b'\x80\x04\x95\x0f\x06\x00\x00\x00\x00\x00\x00\x8c\ndill._dill\x94\x8c\x10_create_function\x94\x93\x94(h\x00\x8c\x0c_create_code\x94\x93\x94(K\x01K\x00K\x00K\x05K\x03KGC4d\x01d\x02l\x00m\x01}\x02m\x02}\x03\x01\x00|\x02\xa0\x03d\x03\xa1\x01s\x11|\x03d\x04\x83\x01S\x00t\x04\xa0\x05d\x05\xa1\x01}\x04|\x04\xa0\x06\xa1\x00S\x00\x94(NK\x00\x8c\x07session\x94\x8c\x08redirect\x94\x86\x94\x8c\x08username\x94\x8c\x01/\x94\x8c\x0fcalculator.html\x94t\x94(\x8c\x05flask\x94h\x06h\x07\x8c\x03get\x94\x8c\x05webpy\x94\x8c\x0bdocumentify\x94\x8c\n_stringify\x94t\x94(\x8c\x03app\x94\x8c\x04args\x94h\x06h\x07\x8c\x08document\x94t\x94\x8c\x08<string>\x94\x8c\x07handler\x94K\x04C\x08\x00\x01\x10\x02\x12\x02\n\x02\x94))t\x94R\x94}\x94\x8c\x08__name__\x94Nsh\x18NNt\x94R\x94}\x94}\x94\x8c\x0f__annotations__\x94}\x94h\x13\x8c\tflask.app\x94\x8c\x05Flask\x94\x93\x94ss\x86\x94bh\x1c(\x8c\x0c__builtins__\x94cbuiltins\n__dict__\nh\x0fh\x00\x8c\x0e_import_module\x94\x93\x94\x8c\x05webpy\x94\x85\x94R\x94}\x94(h\x1dh+\x8c\x07__doc__\x94N\x8c\x0b__package__\x94h+\x8c\x08__spec__\x94\x8c\x11_frozen_importlib\x94\x8c\nModuleSpec\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94h+\x8c\x06loader\x94\x8c\x1a_frozen_importlib_external\x94\x8c\x10SourceFileLoader\x94\x93\x94)\x81\x94}\x94(h7h+\x8c\x04path\x94\x8c/C:\\Users\\carlf\\programs\\webpy\\webpy\\__init__.py\x94ub\x8c\x06origin\x94h?\x8c\x0cloader_state\x94N\x8c\x1asubmodule_search_locations\x94]\x94\x8c#C:\\Users\\carlf\\programs\\webpy\\webpy\x94a\x8c\r_set_fileattr\x94\x88\x8c\x07_cached\x94\x8cHC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\__init__.cpython-310.pyc\x94\x8c\r_initializing\x94\x89ub\x8c\x08__path__\x94hC\x8c\x08__file__\x94h?\x8c\n__cached__\x94hG\x8c\x0frender_template\x94\x8c\x10flask.templating\x94hL\x93\x94h%h&\x8c\x07partial\x94h\x00\x8c\n_load_type\x94\x93\x94\x8c\x0bPartialType\x94\x85\x94R\x94\x8c\x0cFunctionType\x94hQ\x8c\nLambdaType\x94\x85\x94R\x94\x8c\x16make_document_from_str\x94\x8c\x06domapi\x94hY\x93\x94h\x10h+h\x10\x93\x94\x8c\x07appbind\x94h+h]\x93\x94\x8c\tfs_routes\x94h*\x8c\x0fwebpy.fs_routes\x94\x85\x94R\x94}\x94(h\x1dh`h/Nh0\x8c\x05webpy\x94h1h4)\x81\x94}\x94(h7h`h8h;)\x81\x94}\x94(h7h`h>\x8c0C:\\Users\\carlf\\programs\\webpy\\webpy\\fs_routes.py\x94ubh@hihANhBNhE\x88hF\x8cIC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\fs_routes.cpython-310.pyc\x94hH\x89ubhJhihKhj\x8c\x02os\x94h*hk\x85\x94R\x94\x8c\x04json\x94h*hn\x85\x94R\x94\x8c\x04dill\x94h*hq\x85\x94R\x94h]h^h%h&hOhT\x8c\x0bROUTE_FUNCS\x94}\x94\x8c\x06Module\x94h`hv\x93\x94\x8c\nmodularize\x94h`hx\x93\x94\x8c\x0fparse_fs_routes\x94h`hz\x93\x94\x8c\x13__warningregistry__\x94}\x94\x8c\x07version\x94K\x00sububh%h&h\x18h\x1fu0.'),A,'/calculator/_handler'))
A.route('/dashboard/',**{D:[E]})(C.appbind(B.loads(b'\x80\x04\x95\x10\x06\x00\x00\x00\x00\x00\x00\x8c\ndill._dill\x94\x8c\x10_create_function\x94\x93\x94(h\x00\x8c\x0c_create_code\x94\x93\x94(K\x01K\x00K\x00K\x05K\x03KGC4d\x01d\x02l\x00m\x01}\x02m\x02}\x03\x01\x00|\x02\xa0\x03d\x03\xa1\x01s\x11|\x03d\x04\x83\x01S\x00t\x04\xa0\x05d\x05\xa1\x01}\x04|\x04\xa0\x06\xa1\x00S\x00\x94(NK\x00\x8c\x07session\x94\x8c\x08redirect\x94\x86\x94\x8c\x08username\x94\x8c\x01/\x94\x8c\x0edashboard.html\x94t\x94(\x8c\x05flask\x94h\x06h\x07\x8c\x03get\x94\x8c\x05webpy\x94\x8c\x0bdocumentify\x94\x8c\n_stringify\x94t\x94(\x8c\x03app\x94\x8c\x04args\x94h\x06h\x07\x8c\x08document\x94t\x94\x8c\x08<string>\x94\x8c\x07handler\x94K\x04C\n\x00\x01\x10\x02\n\x01\x08\x02\n\x02\x94))t\x94R\x94}\x94\x8c\x08__name__\x94Nsh\x18NNt\x94R\x94}\x94}\x94\x8c\x0f__annotations__\x94}\x94h\x13\x8c\tflask.app\x94\x8c\x05Flask\x94\x93\x94ss\x86\x94bh\x1c(\x8c\x0c__builtins__\x94cbuiltins\n__dict__\nh\x0fh\x00\x8c\x0e_import_module\x94\x93\x94\x8c\x05webpy\x94\x85\x94R\x94}\x94(h\x1dh+\x8c\x07__doc__\x94N\x8c\x0b__package__\x94h+\x8c\x08__spec__\x94\x8c\x11_frozen_importlib\x94\x8c\nModuleSpec\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94h+\x8c\x06loader\x94\x8c\x1a_frozen_importlib_external\x94\x8c\x10SourceFileLoader\x94\x93\x94)\x81\x94}\x94(h7h+\x8c\x04path\x94\x8c/C:\\Users\\carlf\\programs\\webpy\\webpy\\__init__.py\x94ub\x8c\x06origin\x94h?\x8c\x0cloader_state\x94N\x8c\x1asubmodule_search_locations\x94]\x94\x8c#C:\\Users\\carlf\\programs\\webpy\\webpy\x94a\x8c\r_set_fileattr\x94\x88\x8c\x07_cached\x94\x8cHC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\__init__.cpython-310.pyc\x94\x8c\r_initializing\x94\x89ub\x8c\x08__path__\x94hC\x8c\x08__file__\x94h?\x8c\n__cached__\x94hG\x8c\x0frender_template\x94\x8c\x10flask.templating\x94hL\x93\x94h%h&\x8c\x07partial\x94h\x00\x8c\n_load_type\x94\x93\x94\x8c\x0bPartialType\x94\x85\x94R\x94\x8c\x0cFunctionType\x94hQ\x8c\nLambdaType\x94\x85\x94R\x94\x8c\x16make_document_from_str\x94\x8c\x06domapi\x94hY\x93\x94h\x10h+h\x10\x93\x94\x8c\x07appbind\x94h+h]\x93\x94\x8c\tfs_routes\x94h*\x8c\x0fwebpy.fs_routes\x94\x85\x94R\x94}\x94(h\x1dh`h/Nh0\x8c\x05webpy\x94h1h4)\x81\x94}\x94(h7h`h8h;)\x81\x94}\x94(h7h`h>\x8c0C:\\Users\\carlf\\programs\\webpy\\webpy\\fs_routes.py\x94ubh@hihANhBNhE\x88hF\x8cIC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\fs_routes.cpython-310.pyc\x94hH\x89ubhJhihKhj\x8c\x02os\x94h*hk\x85\x94R\x94\x8c\x04json\x94h*hn\x85\x94R\x94\x8c\x04dill\x94h*hq\x85\x94R\x94h]h^h%h&hOhT\x8c\x0bROUTE_FUNCS\x94}\x94\x8c\x06Module\x94h`hv\x93\x94\x8c\nmodularize\x94h`hx\x93\x94\x8c\x0fparse_fs_routes\x94h`hz\x93\x94\x8c\x13__warningregistry__\x94}\x94\x8c\x07version\x94K\x00sububh%h&h\x18h\x1fu0.'),A,'/dashboard/_handler'))
A.route('/game/',**{D:[E]})(C.appbind(B.loads(b'\x80\x04\x957\x0c\x00\x00\x00\x00\x00\x00\x8c\ndill._dill\x94\x8c\x10_create_function\x94\x93\x94(h\x00\x8c\x0c_create_code\x94\x93\x94(K\x01K\x00K\x00K\x05K\x14KGB\x14\x01\x00\x00d\x01d\x02l\x00m\x01}\x02m\x02}\x03\x01\x00|\x02\xa0\x03d\x03\xa1\x01s\x11|\x03d\x04\x83\x01S\x00|\x02\xa0\x03d\x03\xa1\x01}\x04t\x04d\x1dd\x05t\x04d\x1dd\x06t\x05d\x1dd\x07t\x06d\x1dd\x08g\x00i\x01d\td\nd\x0b\x9c\x02\xa4\x01\x8e\x01t\x07d\x1dd\x08g\x00i\x01d\x0cd\rd\x0e\x9c\x02\xa4\x01\x8e\x01t\x07d\x1dd\x08g\x00i\x01d\x0cd\x0fd\x0e\x9c\x02\xa4\x01\x8e\x01t\x08d\x1dd\x10g\x00d\x11\x9c\x02i\x00\xa4\x01\x8e\x01g\x04d\x11\x9c\x02i\x00\xa4\x01\x8e\x01t\td\x1dd\x07t\nd\x1dd\x08g\x00i\x01d\x12|\x04d\x13\x9c\x02\xa4\x01\x8e\x01t\x0bd\x1dd\x14t\x0cd\x1dd\x08g\x00i\x01d\x15d\x16d\x17\x9c\x02\xa4\x01\x8e\x01g\x01d\x11\x9c\x02d\x18d\x19i\x01\xa4\x01\x8e\x01g\x02d\x11\x9c\x02d\x1ad\x1bd\x1c\x9c\x02\xa4\x01\x8e\x01g\x02d\x11\x9c\x02i\x00\xa4\x01\x8e\x01g\x01d\x11\x9c\x02i\x00\xa4\x01\x8e\x01j\x04S\x00\x94(NK\x00\x8c\x07session\x94\x8c\x08redirect\x94\x86\x94\x8c\x08username\x94\x8c\x01/\x94\x8c\x03\n\t\t\x94\x8c\x04\n\t\t\t\x94\x8c\x05\n\t\t\t\t\x94\x8c\x08children\x94\x8c\x14../static/js/game.js\x94\x8c\x00\x94\x8c\x03src\x94\x8c\x05defer\x94\x86\x94\x8c\nstylesheet\x94\x8c\x17../static/css/theme.css\x94\x8c\x03rel\x94\x8c\x04href\x94\x86\x94\x8c\x16../static/css/game.css\x94\x8c\x04Game\x94\x8c\x04data\x94h\x0e\x86\x94\x8c\tgametitle\x94\x8c\x02id\x94\x8c\x04name\x94\x86\x94\x8c\x07\n\t\t\t\t\t\t\x94\x8c\x06player\x94\x8c\x1b../static/images/player.png\x94h\x1eh\x11\x86\x94h\x1e\x8c\x08gamearea\x94\x8c\x0bpage-center\x94\x8c"overflow: hidden; padding-top: 5%;\x94\x8c\x05class\x94\x8c\x05style\x94\x86\x94)t\x94(\x8c\x05flask\x94h\x06h\x07\x8c\x03get\x94\x8c\x04html\x94\x8c\x04head\x94\x8c\x06script\x94\x8c\x04link\x94\x8c\x05title\x94\x8c\x04body\x94\x8c\x02h1\x94\x8c\x06canvas\x94\x8c\x03img\x94t\x94(\x8c\x03app\x94\x8c\x04args\x94h\x06h\x07h\tt\x94\x8c\x08<string>\x94\x8c\x07handler\x94K\x04C\n\x00\x01\x10\x02\x12\x02\n\x03\xe6\xff\x94))t\x94R\x94}\x94\x8c\x08__name__\x94Nsh<NNt\x94R\x94}\x94}\x94\x8c\x0f__annotations__\x94}\x94h8\x8c\tflask.app\x94\x8c\x05Flask\x94\x93\x94ss\x86\x94bh@(\x8c\x0c__builtins__\x94cbuiltins\n__dict__\n\x8c\rstandard_tags\x94]\x94(\x8c\x01a\x94\x8c\x04abbr\x94\x8c\x07acronym\x94\x8c\x07address\x94\x8c\x06applet\x94\x8c\x04area\x94\x8c\x07article\x94\x8c\x05aside\x94\x8c\x05audio\x94\x8c\x01b\x94\x8c\x04base\x94\x8c\x08basefont\x94\x8c\x03bdi\x94\x8c\x03bdo\x94\x8c\x07bgsound\x94\x8c\x03big\x94\x8c\x05blink\x94\x8c\nblockquote\x94h3\x8c\x02br\x94\x8c\x06button\x94h5\x8c\x07caption\x94\x8c\x06center\x94\x8c\x04cite\x94\x8c\x04code\x94\x8c\x03col\x94\x8c\x08colgroup\x94\x8c\x07content\x94h\x1b\x8c\x08datalist\x94\x8c\x02dd\x94\x8c\tdecorator\x94\x8c\x03del\x94\x8c\x07details\x94\x8c\x03dfn\x94\x8c\x03dir\x94\x8c\x03div\x94\x8c\x02dl\x94\x8c\x02dt\x94\x8c\x07element\x94\x8c\x02em\x94\x8c\x05embed\x94\x8c\x08fieldset\x94\x8c\nfigcaption\x94\x8c\x06figure\x94\x8c\x04font\x94\x8c\x06footer\x94\x8c\x04form\x94\x8c\x05frame\x94\x8c\x08frameset\x94h4\x8c\x02h2\x94\x8c\x02h3\x94\x8c\x02h4\x94\x8c\x02h5\x94\x8c\x02h6\x94h/\x8c\x06header\x94\x8c\x06hgroup\x94\x8c\x02hr\x94h.\x8c\x01i\x94\x8c\x06iframe\x94h6\x8c\x05input\x94\x8c\x03ins\x94\x8c\x07isindex\x94\x8c\x03kbd\x94\x8c\x06keygen\x94\x8c\x05label\x94\x8c\x06legend\x94\x8c\x02li\x94h1\x8c\x07listing\x94\x8c\x04main\x94\x8c\x03map\x94\x8c\x04mark\x94\x8c\x07marquee\x94\x8c\x04menu\x94\x8c\x08menuitem\x94\x8c\x04meta\x94\x8c\x05meter\x94\x8c\x03nav\x94\x8c\x04nobr\x94\x8c\x08noframes\x94\x8c\x08noscript\x94\x8c\x06object\x94\x8c\x02ol\x94\x8c\x08optgroup\x94\x8c\x06option\x94\x8c\x06output\x94\x8c\x01p\x94\x8c\x05param\x94\x8c\tplaintext\x94\x8c\x03pre\x94\x8c\x08progress\x94\x8c\x01q\x94\x8c\x02rp\x94\x8c\x02rt\x94\x8c\x04ruby\x94\x8c\x01s\x94\x8c\x04samp\x94h0\x8c\x07section\x94\x8c\x06select\x94\x8c\x06shadow\x94\x8c\x05small\x94\x8c\x06source\x94\x8c\x06spacer\x94\x8c\x04span\x94\x8c\x06strike\x94\x8c\x06strong\x94h)\x8c\x03sub\x94\x8c\x07summary\x94\x8c\x03sup\x94\x8c\x05table\x94\x8c\x05tbody\x94\x8c\x02td\x94\x8c\x08template\x94\x8c\x08textarea\x94\x8c\x05tfoot\x94\x8c\x02th\x94\x8c\x05thead\x94\x8c\x04time\x94h2\x8c\x02tr\x94\x8c\x05track\x94\x8c\x02tt\x94\x8c\x01u\x94\x8c\x02ul\x94\x8c\x03var\x94\x8c\x05video\x94\x8c\x03wbr\x94\x8c\x03xmp\x94e\x8c\x07Element\x94\x8c\x0bpysite.tags\x94h\xcc\x93\x94\x8c\x03tag\x94h\xcbhOh\xcdhO\x93\x94hPh\xcdhP\x93\x94hQh\xcdhQ\x93\x94hRh\xcdhR\x93\x94hSh\xcdhS\x93\x94hTh\xcdhT\x93\x94hUh\xcdhU\x93\x94hVh\xcdhV\x93\x94hWh\xcdhW\x93\x94hXh\xcdhX\x93\x94hYh\xcdhY\x93\x94hZh\xcdhZ\x93\x94h[h\xcdh[\x93\x94h\\h\xcdh\\\x93\x94h]h\xcdh]\x93\x94h^h\xcdh^\x93\x94h_h\xcdh_\x93\x94h`h\xcdh`\x93\x94h3h\xcdh3\x93\x94hah\xcdha\x93\x94hbh\xcdhb\x93\x94h5h\xcdh5\x93\x94hch\xcdhc\x93\x94hdh\xcdhd\x93\x94heh\xcdhe\x93\x94hfh\xcdhf\x93\x94hgh\xcdhg\x93\x94hhh\xcdhh\x93\x94hih\xcdhi\x93\x94h\x1bh\xcdh\x1b\x93\x94hjh\xcdhj\x93\x94hkh\xcdhk\x93\x94hlh\xcdhl\x93\x94hmh\xcdhm\x93\x94hnh\xcdhn\x93\x94hoh\xcdho\x93\x94hph\xcdhp\x93\x94hqh\xcdhq\x93\x94hrh\xcdhr\x93\x94hsh\xcdhs\x93\x94hth\xcdht\x93\x94huh\xcdhu\x93\x94hvh\xcdhv\x93\x94hwh\xcdhw\x93\x94hxh\xcdhx\x93\x94hyh\xcdhy\x93\x94hzh\xcdhz\x93\x94h{h\xcdh{\x93\x94h|h\xcdh|\x93\x94h}h\xcdh}\x93\x94h~h\xcdh~\x93\x94h4h\xcdh4\x93\x94h\x7fh\xcdh\x7f\x93\x94h\x80h\xcdh\x80\x93\x94h\x81h\xcdh\x81\x93\x94h\x82h\xcdh\x82\x93\x94h\x83h\xcdh\x83\x93\x94h/h\xcdh/\x93\x94h\x84h\xcdh\x84\x93\x94h\x85h\xcdh\x85\x93\x94h\x86h\xcdh\x86\x93\x94h.h\xcdh.\x93\x94h\x87h\xcdh\x87\x93\x94h\x88h\xcdh\x88\x93\x94h6h\xcdh6\x93\x94h\x89h\xcdh\x89\x93\x94h\x8ah\xcdh\x8a\x93\x94h\x8bh\xcdh\x8b\x93\x94h\x8ch\xcdh\x8c\x93\x94h\x8dh\xcdh\x8d\x93\x94h\x8eh\xcdh\x8e\x93\x94h\x8fh\xcdh\x8f\x93\x94h\x90h\xcdh\x90\x93\x94h1h\xcdh1\x93\x94h\x91h\xcdh\x91\x93\x94h\x92h\xcdh\x92\x93\x94h\x93h\xcdh\x93\x93\x94h\x94h\xcdh\x94\x93\x94h\x95h\xcdh\x95\x93\x94h\x96h\xcdh\x96\x93\x94h\x97h\xcdh\x97\x93\x94h\x98h\xcdh\x98\x93\x94h\x99h\xcdh\x99\x93\x94h\x9ah\xcdh\x9a\x93\x94h\x9bh\xcdh\x9b\x93\x94h\x9ch\xcdh\x9c\x93\x94h\x9dh\xcdh\x9d\x93\x94h\x9eh\xcdh\x9e\x93\x94h\x9fh\xcdh\x9f\x93\x94h\xa0h\xcdh\xa0\x93\x94h\xa1h\xcdh\xa1\x93\x94h\xa2h\xcdh\xa2\x93\x94h\xa3h\xcdh\xa3\x93\x94h\xa4h\xcdh\xa4\x93\x94h\xa5h\xcdh\xa5\x93\x94h\xa6h\xcdh\xa6\x93\x94h\xa7h\xcdh\xa7\x93\x94h\xa8h\xcdh\xa8\x93\x94h\xa9h\xcdh\xa9\x93\x94h\xaah\xcdh\xaa\x93\x94h\xabh\xcdh\xab\x93\x94h\xach\xcdh\xac\x93\x94h\xadh\xcdh\xad\x93\x94h0h\xcdh0\x93\x94h\xaeh\xcdh\xae\x93\x94h\xafh\xcdh\xaf\x93\x94h\xb0h\xcdh\xb0\x93\x94h\xb1h\xcdh\xb1\x93\x94h\xb2h\xcdh\xb2\x93\x94h\xb3h\xcdh\xb3\x93\x94h\xb4h\xcdh\xb4\x93\x94h\xb5h\xcdh\xb5\x93\x94h\xb6h\xcdh\xb6\x93\x94h)h\xcdh)\x93\x94h\xb7h\xcdh\xb7\x93\x94h\xb8h\xcdh\xb8\x93\x94h\xb9h\xcdh\xb9\x93\x94h\xbah\xcdh\xba\x93\x94h\xbbh\xcdh\xbb\x93\x94h\xbch\xcdh\xbc\x93\x94h\xbdh\xcdh\xbd\x93\x94h\xbeh\xcdh\xbe\x93\x94h\xbfh\xcdh\xbf\x93\x94h\xc0h\xcdh\xc0\x93\x94h\xc1h\xcdh\xc1\x93\x94h\xc2h\xcdh\xc2\x93\x94h2h\xcdh2\x93\x94h\xc3h\xcdh\xc3\x93\x94h\xc4h\xcdh\xc4\x93\x94h\xc5h\xcdh\xc5\x93\x94h\xc6h\xcdh\xc6\x93\x94h\xc7h\xcdh\xc7\x93\x94h\xc8h\xcdh\xc8\x93\x94h\xc9h\xcdh\xc9\x93\x94h\xcah\xcdh\xca\x93\x94h\xcbh\xcdh\xcb\x93\x94hIhJh<hCu0.'),A,'/game/_handler'))
A.route('/login/',**{D:['POST']})(C.appbind(B.loads(b'\x80\x04\x95M\x10\x00\x00\x00\x00\x00\x00\x8c\ndill._dill\x94\x8c\x10_create_function\x94\x93\x94(h\x00\x8c\x0c_create_code\x94\x93\x94(K\x01K\x00K\x00K\x06K\x04KGC>d\x01d\x02l\x00m\x01}\x02m\x02}\x03\x01\x00|\x02j\x03\xa0\x04d\x03\xa1\x01|\x02j\x03\xa0\x04d\x04\xa1\x01\x02\x02}\x04}\x05|\x04|\x03d\x03<\x00|\x05|\x03d\x04<\x00d\x05S\x00\x94(NK\x00\x8c\x07request\x94\x8c\x07session\x94\x86\x94\x8c\x08username\x94\x8c\x08password\x94\x8c\x00\x94t\x94(\x8c\x05flask\x94h\x06h\x07\x8c\x04json\x94\x8c\x03get\x94t\x94(\x8c\x03app\x94\x8c\x04args\x94h\x06h\x07h\th\nt\x94\x8c\x08<string>\x94\x8c\x07handler\x94K\x05C\x0c\x00\x01\x10\x03\x16\xff\x04\x03\x08\x01\x08\x02\x94))t\x94R\x94}\x94\x8c\x08__name__\x94Nsh\x15NNt\x94R\x94}\x94}\x94\x8c\x0f__annotations__\x94}\x94h\x11\x8c\tflask.app\x94\x8c\x05Flask\x94\x93\x94ss\x86\x94bh\x19(\x8c\x0c__builtins__\x94cbuiltins\n__dict__\n\x8c\x05webpy\x94h\x00\x8c\x0e_import_module\x94\x93\x94\x8c\x05webpy\x94\x85\x94R\x94}\x94(h\x1ah)\x8c\x07__doc__\x94N\x8c\x0b__package__\x94h)\x8c\x08__spec__\x94\x8c\x11_frozen_importlib\x94\x8c\nModuleSpec\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94h)\x8c\x06loader\x94\x8c\x1a_frozen_importlib_external\x94\x8c\x10SourceFileLoader\x94\x93\x94)\x81\x94}\x94(h5h)\x8c\x04path\x94\x8c/C:\\Users\\carlf\\programs\\webpy\\webpy\\__init__.py\x94ub\x8c\x06origin\x94h=\x8c\x0cloader_state\x94N\x8c\x1asubmodule_search_locations\x94]\x94\x8c#C:\\Users\\carlf\\programs\\webpy\\webpy\x94a\x8c\r_set_fileattr\x94\x88\x8c\x07_cached\x94\x8cHC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\__init__.cpython-310.pyc\x94\x8c\r_initializing\x94\x89ub\x8c\x08__path__\x94hA\x8c\x08__file__\x94h=\x8c\n__cached__\x94hE\x8c\x0frender_template\x94\x8c\x10flask.templating\x94hJ\x93\x94h"h#\x8c\x07partial\x94h\x00\x8c\n_load_type\x94\x93\x94\x8c\x0bPartialType\x94\x85\x94R\x94\x8c\x0cFunctionType\x94hO\x8c\nLambdaType\x94\x85\x94R\x94\x8c\x16make_document_from_str\x94\x8c\x06domapi\x94hW\x93\x94\x8c\x0bdocumentify\x94h)hZ\x93\x94\x8c\x07appbind\x94h)h\\\x93\x94\x8c\tfs_routes\x94h(\x8c\x0fwebpy.fs_routes\x94\x85\x94R\x94}\x94(h\x1ah_h-Nh.\x8c\x05webpy\x94h/h2)\x81\x94}\x94(h5h_h6h9)\x81\x94}\x94(h5h_h<\x8c0C:\\Users\\carlf\\programs\\webpy\\webpy\\fs_routes.py\x94ubh>hhh?Nh@NhC\x88hD\x8cIC:\\Users\\carlf\\programs\\webpy\\webpy\\__pycache__\\fs_routes.cpython-310.pyc\x94hF\x89ubhHhhhIhi\x8c\x02os\x94h(hj\x85\x94R\x94h\x0eh(h\x0e\x85\x94R\x94\x8c\x04dill\x94h(ho\x85\x94R\x94h\\h]h"h#hMhR\x8c\x0bROUTE_FUNCS\x94}\x94\x8c\x06Module\x94h_ht\x93\x94\x8c\nmodularize\x94h_hv\x93\x94\x8c\x0fparse_fs_routes\x94h_hx\x93\x94\x8c\x13__warningregistry__\x94}\x94\x8c\x07version\x94K\x00subub\x8c\rstandard_tags\x94]\x94(\x8c\x01a\x94\x8c\x04abbr\x94\x8c\x07acronym\x94\x8c\x07address\x94\x8c\x06applet\x94\x8c\x04area\x94\x8c\x07article\x94\x8c\x05aside\x94\x8c\x05audio\x94\x8c\x01b\x94\x8c\x04base\x94\x8c\x08basefont\x94\x8c\x03bdi\x94\x8c\x03bdo\x94\x8c\x07bgsound\x94\x8c\x03big\x94\x8c\x05blink\x94\x8c\nblockquote\x94\x8c\x04body\x94\x8c\x02br\x94\x8c\x06button\x94\x8c\x06canvas\x94\x8c\x07caption\x94\x8c\x06center\x94\x8c\x04cite\x94\x8c\x04code\x94\x8c\x03col\x94\x8c\x08colgroup\x94\x8c\x07content\x94\x8c\x04data\x94\x8c\x08datalist\x94\x8c\x02dd\x94\x8c\tdecorator\x94\x8c\x03del\x94\x8c\x07details\x94\x8c\x03dfn\x94\x8c\x03dir\x94\x8c\x03div\x94\x8c\x02dl\x94\x8c\x02dt\x94\x8c\x07element\x94\x8c\x02em\x94\x8c\x05embed\x94\x8c\x08fieldset\x94\x8c\nfigcaption\x94\x8c\x06figure\x94\x8c\x04font\x94\x8c\x06footer\x94\x8c\x04form\x94\x8c\x05frame\x94\x8c\x08frameset\x94\x8c\x02h1\x94\x8c\x02h2\x94\x8c\x02h3\x94\x8c\x02h4\x94\x8c\x02h5\x94\x8c\x02h6\x94\x8c\x04head\x94\x8c\x06header\x94\x8c\x06hgroup\x94\x8c\x02hr\x94\x8c\x04html\x94\x8c\x01i\x94\x8c\x06iframe\x94\x8c\x03img\x94\x8c\x05input\x94\x8c\x03ins\x94\x8c\x07isindex\x94\x8c\x03kbd\x94\x8c\x06keygen\x94\x8c\x05label\x94\x8c\x06legend\x94\x8c\x02li\x94\x8c\x04link\x94\x8c\x07listing\x94\x8c\x04main\x94\x8c\x03map\x94\x8c\x04mark\x94\x8c\x07marquee\x94\x8c\x04menu\x94\x8c\x08menuitem\x94\x8c\x04meta\x94\x8c\x05meter\x94\x8c\x03nav\x94\x8c\x04nobr\x94\x8c\x08noframes\x94\x8c\x08noscript\x94\x8c\x06object\x94\x8c\x02ol\x94\x8c\x08optgroup\x94\x8c\x06option\x94\x8c\x06output\x94\x8c\x01p\x94\x8c\x05param\x94\x8c\tplaintext\x94\x8c\x03pre\x94\x8c\x08progress\x94\x8c\x01q\x94\x8c\x02rp\x94\x8c\x02rt\x94\x8c\x04ruby\x94\x8c\x01s\x94\x8c\x04samp\x94\x8c\x06script\x94\x8c\x07section\x94\x8c\x06select\x94\x8c\x06shadow\x94\x8c\x05small\x94\x8c\x06source\x94\x8c\x06spacer\x94\x8c\x04span\x94\x8c\x06strike\x94\x8c\x06strong\x94\x8c\x05style\x94\x8c\x03sub\x94\x8c\x07summary\x94\x8c\x03sup\x94\x8c\x05table\x94\x8c\x05tbody\x94\x8c\x02td\x94\x8c\x08template\x94\x8c\x08textarea\x94\x8c\x05tfoot\x94\x8c\x02th\x94\x8c\x05thead\x94\x8c\x04time\x94\x8c\x05title\x94\x8c\x02tr\x94\x8c\x05track\x94\x8c\x02tt\x94\x8c\x01u\x94\x8c\x02ul\x94\x8c\x03var\x94\x8c\x05video\x94\x8c\x03wbr\x94\x8c\x03xmp\x94e\x8c\x07Element\x94\x8c\x0bpysite.tags\x94j\x07\x01\x00\x00\x93\x94\x8c\x03tag\x94j\x06\x01\x00\x00h\x7fj\x08\x01\x00\x00h\x7f\x93\x94h\x80j\x08\x01\x00\x00h\x80\x93\x94h\x81j\x08\x01\x00\x00h\x81\x93\x94h\x82j\x08\x01\x00\x00h\x82\x93\x94h\x83j\x08\x01\x00\x00h\x83\x93\x94h\x84j\x08\x01\x00\x00h\x84\x93\x94h\x85j\x08\x01\x00\x00h\x85\x93\x94h\x86j\x08\x01\x00\x00h\x86\x93\x94h\x87j\x08\x01\x00\x00h\x87\x93\x94h\x88j\x08\x01\x00\x00h\x88\x93\x94h\x89j\x08\x01\x00\x00h\x89\x93\x94h\x8aj\x08\x01\x00\x00h\x8a\x93\x94h\x8bj\x08\x01\x00\x00h\x8b\x93\x94h\x8cj\x08\x01\x00\x00h\x8c\x93\x94h\x8dj\x08\x01\x00\x00h\x8d\x93\x94h\x8ej\x08\x01\x00\x00h\x8e\x93\x94h\x8fj\x08\x01\x00\x00h\x8f\x93\x94h\x90j\x08\x01\x00\x00h\x90\x93\x94h\x91j\x08\x01\x00\x00h\x91\x93\x94h\x92j\x08\x01\x00\x00h\x92\x93\x94h\x93j\x08\x01\x00\x00h\x93\x93\x94h\x94j\x08\x01\x00\x00h\x94\x93\x94h\x95j\x08\x01\x00\x00h\x95\x93\x94h\x96j\x08\x01\x00\x00h\x96\x93\x94h\x97j\x08\x01\x00\x00h\x97\x93\x94h\x98j\x08\x01\x00\x00h\x98\x93\x94h\x99j\x08\x01\x00\x00h\x99\x93\x94h\x9aj\x08\x01\x00\x00h\x9a\x93\x94h\x9bj\x08\x01\x00\x00h\x9b\x93\x94h\x9cj\x08\x01\x00\x00h\x9c\x93\x94h\x9dj\x08\x01\x00\x00h\x9d\x93\x94h\x9ej\x08\x01\x00\x00h\x9e\x93\x94h\x9fj\x08\x01\x00\x00h\x9f\x93\x94h\xa0j\x08\x01\x00\x00h\xa0\x93\x94h\xa1j\x08\x01\x00\x00h\xa1\x93\x94h\xa2j\x08\x01\x00\x00h\xa2\x93\x94h\xa3j\x08\x01\x00\x00h\xa3\x93\x94h\xa4j\x08\x01\x00\x00h\xa4\x93\x94h\xa5j\x08\x01\x00\x00h\xa5\x93\x94h\xa6j\x08\x01\x00\x00h\xa6\x93\x94h\xa7j\x08\x01\x00\x00h\xa7\x93\x94h\xa8j\x08\x01\x00\x00h\xa8\x93\x94h\xa9j\x08\x01\x00\x00h\xa9\x93\x94h\xaaj\x08\x01\x00\x00h\xaa\x93\x94h\xabj\x08\x01\x00\x00h\xab\x93\x94h\xacj\x08\x01\x00\x00h\xac\x93\x94h\xadj\x08\x01\x00\x00h\xad\x93\x94h\xaej\x08\x01\x00\x00h\xae\x93\x94h\xafj\x08\x01\x00\x00h\xaf\x93\x94h\xb0j\x08\x01\x00\x00h\xb0\x93\x94h\xb1j\x08\x01\x00\x00h\xb1\x93\x94h\xb2j\x08\x01\x00\x00h\xb2\x93\x94h\xb3j\x08\x01\x00\x00h\xb3\x93\x94h\xb4j\x08\x01\x00\x00h\xb4\x93\x94h\xb5j\x08\x01\x00\x00h\xb5\x93\x94h\xb6j\x08\x01\x00\x00h\xb6\x93\x94h\xb7j\x08\x01\x00\x00h\xb7\x93\x94h\xb8j\x08\x01\x00\x00h\xb8\x93\x94h\xb9j\x08\x01\x00\x00h\xb9\x93\x94h\xbaj\x08\x01\x00\x00h\xba\x93\x94h\xbbj\x08\x01\x00\x00h\xbb\x93\x94h\xbcj\x08\x01\x00\x00h\xbc\x93\x94h\xbdj\x08\x01\x00\x00h\xbd\x93\x94h\xbej\x08\x01\x00\x00h\xbe\x93\x94h\xbfj\x08\x01\x00\x00h\xbf\x93\x94h\xc0j\x08\x01\x00\x00h\xc0\x93\x94h\xc1j\x08\x01\x00\x00h\xc1\x93\x94h\xc2j\x08\x01\x00\x00h\xc2\x93\x94h\xc3j\x08\x01\x00\x00h\xc3\x93\x94h\xc4j\x08\x01\x00\x00h\xc4\x93\x94h\xc5j\x08\x01\x00\x00h\xc5\x93\x94h\xc6j\x08\x01\x00\x00h\xc6\x93\x94h\xc7j\x08\x01\x00\x00h\xc7\x93\x94h\xc8j\x08\x01\x00\x00h\xc8\x93\x94h\xc9j\x08\x01\x00\x00h\xc9\x93\x94h\xcaj\x08\x01\x00\x00h\xca\x93\x94h\xcbj\x08\x01\x00\x00h\xcb\x93\x94h\xccj\x08\x01\x00\x00h\xcc\x93\x94h\xcdj\x08\x01\x00\x00h\xcd\x93\x94h\xcej\x08\x01\x00\x00h\xce\x93\x94h\xcfj\x08\x01\x00\x00h\xcf\x93\x94h\xd0j\x08\x01\x00\x00h\xd0\x93\x94h\xd1j\x08\x01\x00\x00h\xd1\x93\x94h\xd2j\x08\x01\x00\x00h\xd2\x93\x94h\xd3j\x08\x01\x00\x00h\xd3\x93\x94h\xd4j\x08\x01\x00\x00h\xd4\x93\x94h\xd5j\x08\x01\x00\x00h\xd5\x93\x94h\xd6j\x08\x01\x00\x00h\xd6\x93\x94h\xd7j\x08\x01\x00\x00h\xd7\x93\x94h\xd8j\x08\x01\x00\x00h\xd8\x93\x94h\xd9j\x08\x01\x00\x00h\xd9\x93\x94h\xdaj\x08\x01\x00\x00h\xda\x93\x94h\xdbj\x08\x01\x00\x00h\xdb\x93\x94h\xdcj\x08\x01\x00\x00h\xdc\x93\x94h\xddj\x08\x01\x00\x00h\xdd\x93\x94h\xdej\x08\x01\x00\x00h\xde\x93\x94h\xdfj\x08\x01\x00\x00h\xdf\x93\x94h\xe0j\x08\x01\x00\x00h\xe0\x93\x94h\xe1j\x08\x01\x00\x00h\xe1\x93\x94h\xe2j\x08\x01\x00\x00h\xe2\x93\x94h\xe3j\x08\x01\x00\x00h\xe3\x93\x94h\xe4j\x08\x01\x00\x00h\xe4\x93\x94h\xe5j\x08\x01\x00\x00h\xe5\x93\x94h\xe6j\x08\x01\x00\x00h\xe6\x93\x94h\xe7j\x08\x01\x00\x00h\xe7\x93\x94h\xe8j\x08\x01\x00\x00h\xe8\x93\x94h\xe9j\x08\x01\x00\x00h\xe9\x93\x94h\xeaj\x08\x01\x00\x00h\xea\x93\x94h\xebj\x08\x01\x00\x00h\xeb\x93\x94h\xecj\x08\x01\x00\x00h\xec\x93\x94h\xedj\x08\x01\x00\x00h\xed\x93\x94h\xeej\x08\x01\x00\x00h\xee\x93\x94h\xefj\x08\x01\x00\x00h\xef\x93\x94h\xf0j\x08\x01\x00\x00h\xf0\x93\x94h\xf1j\x08\x01\x00\x00h\xf1\x93\x94h\xf2j\x08\x01\x00\x00h\xf2\x93\x94h\xf3j\x08\x01\x00\x00h\xf3\x93\x94h\xf4j\x08\x01\x00\x00h\xf4\x93\x94h\xf5j\x08\x01\x00\x00h\xf5\x93\x94h\xf6j\x08\x01\x00\x00h\xf6\x93\x94h\xf7j\x08\x01\x00\x00h\xf7\x93\x94h\xf8j\x08\x01\x00\x00h\xf8\x93\x94h\xf9j\x08\x01\x00\x00h\xf9\x93\x94h\xfaj\x08\x01\x00\x00h\xfa\x93\x94h\xfbj\x08\x01\x00\x00h\xfb\x93\x94h\xfcj\x08\x01\x00\x00h\xfc\x93\x94h\xfdj\x08\x01\x00\x00h\xfd\x93\x94h\xfej\x08\x01\x00\x00h\xfe\x93\x94h\xffj\x08\x01\x00\x00h\xff\x93\x94j\x00\x01\x00\x00j\x08\x01\x00\x00j\x00\x01\x00\x00\x93\x94j\x01\x01\x00\x00j\x08\x01\x00\x00j\x01\x01\x00\x00\x93\x94j\x02\x01\x00\x00j\x08\x01\x00\x00j\x02\x01\x00\x00\x93\x94j\x03\x01\x00\x00j\x08\x01\x00\x00j\x03\x01\x00\x00\x93\x94j\x04\x01\x00\x00j\x08\x01\x00\x00j\x04\x01\x00\x00\x93\x94j\x05\x01\x00\x00j\x08\x01\x00\x00j\x05\x01\x00\x00\x93\x94j\x06\x01\x00\x00j\x08\x01\x00\x00j\x06\x01\x00\x00\x93\x94h"h#h\x15h\x1cu0.'),A,'/login/_handler'))
A.run('127.0.0.1',5000)