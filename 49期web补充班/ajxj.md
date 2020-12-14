# json-ajax

**作用：局部刷新**

```
	<input type="text" name="a">+
	<input type="text" name="b">=
	<input type="text" name="c">
	<input type="button" value="计算">
	<script>jquery链接</script>
	<script>
		var $input = $("input");
		$input.eq(3).click(function{
			var a = $inpur.eq(0).val();
			var b = $inpur.eq(1).val();
			//ajax+json实现数据传送$.ajax(json数据)
			$.ajax({
				"type":"post";(提交数据的提交方式)
				"url":"/test"(路由)-需要重新创建一个新的路由在后台。
				"data":{
					"a":a;
					"b":b;
				},//实现后台的传递
				"success":function(data){
					//console.log(data);//{result:27}
					$input.eq(2).val(data["return"])
				}//成功的函数
				"error":
{}//错误的函数
			});
		});
	</script>
```

**后台**

```
Class Application():
	def get(self,*args,**kwargs):
		self.render("ajax_text.html")
	
	def post(self,*args,**kwargs):
		a = self.get_argument('a')
		b = self.get_argument('b')
		res = float(a) + float(b)
		return_data = {'result':res}#创建类json结构
		self.return(return_data)
		
		
```

