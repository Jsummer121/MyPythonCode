# HTTP协议

&nbsp;&nbsp;&nbsp;&nbsp;在平时我们上网的时候，需要在浏览器中输入一个url（统一资源定位符），然后这个信息会被送往我们所请求的服务器，服务器在根据所请求的东西返回相应的内容。这就是最基本的一个流程。

&nbsp;&nbsp;&nbsp;&nbsp;像这种通过发送请求获取服务器资源的web浏览器等，我们可以称它为**客户端**

&nbsp;&nbsp;&nbsp;&nbsp;web使用一种名为HTTP（超文本传输协议）的协议作为规范，完成从客户端到服务器端等一系列运作流程。

## 一、基础概念

### 1.1 URI和URL

&nbsp;&nbsp;&nbsp;&nbsp;与 URI（统一资源标识符）相比，我们更熟悉 URL（Uniform Resource Locator，统一资源定位符）。URL正是使用 Web 浏览器等 访问 Web 页面时需要输入的网页地址。比如www.baidu.com

&nbsp;&nbsp;&nbsp;&nbsp;URI 是 Uniform Resource Identifier 的缩写。URI 用字符串标识某一互联网资源，而 URL表示资源的地点（互联 网上所处的位置）。可见 URL是 URI 的子集。

### 1.2 请求和响应报文

### 报文基本结构

&nbsp;&nbsp;&nbsp;&nbsp;HTTP 协议的请求和响应报文中必定包含 **HTTP 首部**。首部内容为客户端和服务器分别处理请求和响应提供所需要的信息。对于客户端用户来说，这些信息中的大部分内容都无须亲自查看。报文首部由几个字段构成。 

&nbsp;&nbsp;&nbsp;&nbsp;接着报文首部的是**空行**（在python中用`\r\n表示`）

&nbsp;&nbsp;&nbsp;&nbsp;在空行下面的是**报文主体**，一般在响应报文中出现，即如果你请求一个资源，在响应报文中，你所要的资源（当然如果存在的情况下）就包含在报文主体中。

#### 请求报文

```
GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
```

&nbsp;&nbsp;&nbsp;&nbsp;请求报文是由请求方法、请求 URI、协议版本、可选的请求首部字段和内容实体构成的。

&nbsp;&nbsp;&nbsp;&nbsp;起始行开头的GET表示请求访问服务器的类型，称为方法（method）。随后的字符串 / 指明了请求访问的资源对象，也叫做请求 URI（request-URI）。最后的 HTTP/1.1，即 HTTP 的版本号，用来提示客户端使用的 HTTP 协议功能。 

&nbsp;&nbsp;&nbsp;&nbsp;从第二行开始到最后我们称之为**首部字段**，HTTP 首部字段是构成 HTTP 报文的要素之一。在客户端与服务器之间以 HTTP 协议进行通信的过程中，无论是请求还是响应都会使用首部字段，它能起到传递额外重要信息的作用。（下文会细说） 

&nbsp;&nbsp;&nbsp;&nbsp;综合来看，这段请求内容的意思是：请求访问百度服务器上的/ 页面资源。 

#### 响应报文

```
HTTP/1.1 200 OK
Bdpagetype: 2
Bdqid: 0xc45604fa001c74f2
Cache-Control: private
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html;charset=utf-8
Date: Sat, 26 Dec 2020 06:59:16 GMT
Expires: Sat, 26 Dec 2020 06:59:16 GMT
Server: BWS/1.1
Strict-Transport-Security: max-age=172800
Traceid: 1608965956063549517814147500751221191922
X-Ua-Compatible: IE=Edge,chrome=1
Transfer-Encoding: chunked

<html> ……
```

&nbsp;&nbsp;&nbsp;&nbsp;在起始行开头的 HTTP/1.1 表示服务器对应的 HTTP 版本。 

&nbsp;&nbsp;&nbsp;&nbsp;紧挨着的 200 OK 表示请求的处理结果的状态码（status code）和原因短语（reason-phrase）。下一行显示了创建响应的日期时间，是首部字段（header field）内的一个属性。 

&nbsp;&nbsp;&nbsp;&nbsp;接下来的几行到空行为止都是首部字段。

&nbsp;&nbsp;&nbsp;&nbsp;接着以一空行分隔，之后的内容称为报文主体（entity body）。 

&nbsp;&nbsp;&nbsp;&nbsp;响应报文基本上由协议版本、状态码（表示请求成功或失败的数字代码）、用以解释状态码的原因短语、可选的响应首部字段以及实体主体构成。

## 二、HTTP 方法

&nbsp;&nbsp;&nbsp;&nbsp;客户端发送的请求报文第一行为请求行，包含发送方法字段。

### GET:获取资源

&nbsp;&nbsp;&nbsp;&nbsp;**GET 方法用来请求访问已被 URI 识别的资源**。指定的资源经服务器端解析后返回响应内容。也就是说，如果请求的资源是文本，那就保 持原样返回；如果是像 CGI（Common Gateway Interface，通用网关接口）那样的程序，则返回经过执行后的输出结果。 

### POST: 传输实体主体

&nbsp;&nbsp;&nbsp;&nbsp;**POST 方法用来传输实体的主体**。虽然用 GET 方法也可以传输实体的主体，但一般不用 GET 方法进行传输，而是用 POST 方法。虽说 POST 的功能与 GET 很相似，但POST 的主要目的并不是获取响应的主体内容。 

### PUT： 传输文件

&nbsp;&nbsp;&nbsp;&nbsp;**PUT 方法用来传输文件**。就像 FTP 协议的文件上传一样，要求在请求报文的主体中包含文件内容，然后保存到请求 URI 指定的位置。 但是，鉴于 HTTP/1.1 的 PUT 方法自身不带验证机制，任何人都可以 上传文件 , 存在安全性问题，因此一般的 Web 网站不使用该方法。若配合 Web 应用程序的验证机制，或架构设计采用 REST（REpresentational State Transfer，表征状态转移）标准的同类Web 网站，就可能会开放使用 PUT 方法。 

### HEAD：获得报文首部

&nbsp;&nbsp;&nbsp;&nbsp;HEAD 方法和 GET 方法一样，只是不返回报文主体部分。**用于确认URI 的有效性及资源更新的日期时间等**。

### DELETE:删除文件

&nbsp;&nbsp;&nbsp;&nbsp;DELETE 方法用来删除文件，是与 PUT 相反的方法。DELETE 方法按请求 URI 删除指定的资源。

&nbsp;&nbsp;&nbsp;&nbsp;但是，HTTP/1.1 的 DELETE 方法本身和 PUT 方法一样不带验证机制，所以一般的 Web 网站也不使用 DELETE 方法。当配合 Web 应用程序的验证机制，或遵守 REST 标准时还是有可能会开放使用的。 

### OPTIONS：询问支持的方法

&nbsp;&nbsp;&nbsp;&nbsp;OPTIONS 方法用来查询针对请求 URI 指定的资源支持的方法。

### **TRACE**：追踪路径

&nbsp;&nbsp;&nbsp;&nbsp;TRACE 方法是让 Web 服务器端将之前的请求通信环回给客户端的方法。

&nbsp;&nbsp;&nbsp;&nbsp;发送请求时，在 Max-Forwards 首部字段中填入数值，每经过一个服务器端就将该数字减 1，当数值刚好减到 0 时，就停止继续传输，最后接收到请求的服务器端则返回状态码 200 OK 的响应。 

&nbsp;&nbsp;&nbsp;&nbsp;客户端通过 TRACE 方法可以查询发送出去的请求是怎样被加工修改/ 篡改的。这是因为，请求想要连接到源目标服务器可能会通过代理中转，TRACE 方法就是用来确认连接过程中发生的一系列操作。 

&nbsp;&nbsp;&nbsp;&nbsp;但是，TRACE 方法本来就不怎么常用，再加上它容易引发XST（Cross-Site Tracing，跨站追踪）攻击，通常就更不会用到了。

### **CONNECT**：要求用隧道协议连接代理 

&nbsp;&nbsp;&nbsp;&nbsp;CONNECT 方法要求在与代理服务器通信时建立隧道，实现用隧道协议进行 TCP 通信。主要使用 SSL（Secure Sockets Layer，安全套接层）和 TLS（Transport Layer Security，传输层安全）协议把通信内容加 密后经网络隧道传输。 

### PATCH: 对资源进行部分修改

&nbsp;&nbsp;&nbsp;&nbsp;PUT 也可以用于修改资源，但是只能完全替代原始资源，PATCH 允许部分修改。

## 三、HTTP 状态码

&nbsp;&nbsp;&nbsp;&nbsp;HTTP 状态码负责表示客户端 HTTP 请求的返回结果、标记服务器端的处理是否正常、通知出现的错误等工作

&nbsp;&nbsp;&nbsp;&nbsp;状态码的职责是当客户端向服务器端发送请求时，描述返回的请求结果。借助状态码，用户可以知道服务器端是正常处理了请求，还是出现了错误。数字中的第一位指定了响应类别，后两位无分类。响应类别有以下 5种。

| 状态码 |               类别               |            含义            |
| :----: | :------------------------------: | :------------------------: |
|  1XX   |  Informational（信息性状态码）   |     接收的请求正在处理     |
|  2XX   |      Success（成功状态码）       |      请求正常处理完毕      |
|  3XX   |   Redirection（重定向状态码）    | 需要进行附加操作以完成请求 |
|  4XX   | Client Error（客户端错误状态码） |     服务器无法处理请求     |
|  5XX   | Server Error（服务器错误状态码） |     服务器处理请求出错     |

### **1XX** **信息**

- **100 Continue** ：表明到目前为止都很正常，客户端可以继续发送请求或者忽略这个响应。

### **2XX** **成功**

- **200 OK** ：表示从客户端发来的请求在服务器端被正常处理了。
- **204 No Content** ：请求已经成功处理，但是返回的响应报文不包含实体的主体部分。一般在只需要从客户端往服务器发送信息，而不需要返回数据时使用。
- **206 Partial Content** ：表示客户端进行了范围请求，响应报文包含由 Content-Range 指定范围的实体内容。

### **3XX** **重定向**

- **301 Moved Permanently** ：永久性重定向。该状态码表示请求的资源已被分配了新的 URI，以后应使用资源现在所指的 URI。也就是说，如果已经把资源对应的 URI保存为书签了，这时应该按 Location 首部字段提示的 URI 重新保存。
- **302 Found** ：临时性重定向。该状态码表示请求的资源已被分配了新的 URI，希望用户（本次）能使用新的 URI 访问。 
- **303 See Other** ：和 302 有着相同的功能，但是 303 明确要求客户端应该采用 GET 方法获取资源。

###### 注：虽然 HTTP 协议规定 301、302 状态下重定向时不允许把 POST 方法改成 GET 方法，但是大多数浏览器都会在 301、302 和 303 状态下的重定向把 POST 方法改成 GET 方法。

- **304 Not Modifified** ：如果请求报文首部包含一些条件，例如：If-Match，If-Modifified-Since，If-None-Match，If-Range，If-Unmodifified-Since，如果不满足条件，则服务器会返回 304 状态码。
- **307 Temporary Redirect** ：临时重定向，与 302 的含义类似，但是 307 要求浏览器不会把重定向请求的POST 方法改成 GET 方法。

### **4XX** **客户端错误**

- **400 Bad Request** ：请求报文中存在语法错误。当错误发生时，需修改请求 

  的内容后再次发送请求。另外，浏览器会像 200 OK 一样对待该状态码。

- **401 Unauthorized** ：该状态码表示发送的请求需要有认证信息（BASIC 认证、DIGEST 认证）。如果之前已进行过一次请求，则表示用户认证失败。

- **403 Forbidden** ：该状态码表明对请求资源的访问被服务器拒绝了。服务器端没有必要 给出拒绝的详细理由，但如果想作说明的话，可以在实体的主体部分对原因进行描述，这样就能让用户看到了。 

  未获得文件系统的访问授权，访问权限出现某些问题（从未授权的发送源 IP 地址试图访问）等列举的情况都可能是发生 403 的原因。 

- **404 Not Found** ：该状态码表明服务器上无法找到请求的资源。除此之外，也可以在服务器端拒绝请求且不想说明理由时使用。 

### **5XX** **服务器错误**

- **500 Internal Server Error** ：该状态码表明服务器端在执行请求时发生了错误。也有可能是 Web应用存在的 bug 或某些临时的故障。 
- **503 Service Unavailable** ：服务器暂时处于超负载或正在进行停机维护，现在无法处理请求。

###### 注：状态码和状况的不一致 。不少返回的状态码响应都是错误的，但是用户可能察觉不到这点。比如 Web 应用程序内部发生错误，状态码依然返回 200 OK，这种情况也经常遇到。 

## 四、HTTP首部

&nbsp;&nbsp;&nbsp;&nbsp;有 4 种类型的首部字段：通用首部字段、请求首部字段、响应首部字段和实体首部字段。

### 4.1 首部字段预览

#### 通用首部字段

| 首部字段 | 说明 |
| :------: | :--: |
|Cache-Control |控制缓存的行为|
|Connection |控制不再转发给代理的首部字段、管理持久连接|
|Date |创建报文的日期时间|
|Pragma| 报文指令|
|Trailer| 报文末端的首部一览|
|Transfer-Encoding| 指定报文主体的传输编码方式|
|Upgrade| 升级为其他协议|
|Via |代理服务器的相关信息|
|Warning |错误通知|

#### 请求首部字段

| 首部字段名 | 说明 |
| :--------: | :--: |
|Accept |用户代理可处理的媒体类型|
|Accept-Charset |优先的字符集|
|Accept-Encoding |优先的内容编码|
|Accept-Language |优先的语言（自然语言）|
|Authorization Web| 认证信息|
|Expect |期待服务器的特定行为|
|From| 用户的电子邮箱地址|
|Host |请求资源所在服务器|
|If-Match |比较实体标记（ETag）|
|If-Modified-Since |比较资源的更新时间|
|If-None-Match| 比较实体标记（与 If-Match 相反）|
|If-Range| 资源未更新时发送实体 Byte 的范围请求|
|If-Unmodified-Since |比较资源的更新时间（与 If-Modified-Since 相反）|
|Max-Forwards |最大传输逐跳数|
|Proxy-Authorization |代理服务器要求客户端的认证信息|
|Range |实体的字节范围请求|
|Referer |对请求中 URI 的原始获取方|
|TE |传输编码的优先级|
|User-Agent HTTP| 客户端程序的信息|

#### 响应首部字段

| 首部字段名 | 说明 |
| :--: | :--: |
|Accept-Ranges| 是否接受字节范围请求|
|Age |推算资源创建经过时间|
|ETag| 资源的匹配信息|
|Location |令客户端重定向至指定 URI|
|Proxy-Authenticate |代理服务器对客户端的认证信息|
|Retry-After |对再次发起请求的时机要求|
|Server HTTP |服务器的安装信息|
|Vary |代理服务器缓存的管理信息|
|WWW-Authenticate |服务器对客户端的认证信息|

#### 实体首部字段

| 首部字段名 | 说明 |
| :--: | :--: |
|Allow| 资源可支持的 HTTP 方法|
|Content-Encoding| 实体主体适用的编码方式|
|Content-Language |实体主体的自然语言|
|Content-Length |实体主体的大小|
|Content-Location| 替代对应资源的 URI|
|Content-MD5| 实体主体的报文摘要|
|Content-Range |实体主体的位置范围|
|Content-Type |实体主体的媒体类型|
|Expires |实体主体过期的日期时间|
|Last-Modified |资源的最后修改日期时间|

由于首部字段众多，不需要全记，因此这里只说一下cache的首部。

### 4.2 Cache-Control

&nbsp;&nbsp;&nbsp;&nbsp;通过指定首部字段 Cache-Control 的指令，就能操作缓存的工作机制。 

&nbsp;&nbsp;&nbsp;&nbsp;指令的参数是可选的，多个指令之间通过“,”分隔。首部字段 Cache-Control 的指令可用于请求及响应时。 `Cache-Control: private, max-age=0, no-cache`

&nbsp;&nbsp;&nbsp;&nbsp;可用的指令按请求和响应分类如下所示。

#### 缓存请求指令

| 指令 | 参数 | 说明 |
| :--: | :--: | :--: |
|no-cache |无| 强制向源服务器再次验证|
|no-store |无 |不缓存请求或响应的任何内容|
|max-age = [ 秒]| 必需 |响应的最大Age值 |
|max-stale( = [ 秒])| 可省略| 接收已过期的响应|
|min-fresh = [ 秒] |必需| 期望在指定时间内的响应仍有效|
|no-transform| 无| 代理不可更改媒体类型|
|only-if-cached |无 |从缓存获取资源 |
|cache-extension |- |新指令标记（token）|




#### 缓存响应指令

| 指令 | 参数 | 说明 |
| :--: | :--: | :--: |
|public |无 |可向任意方提供响应的缓存 |
|private| 可省略| 仅向特定用户返回响应 |
|no-cache| 可省略 |缓存前必须先确认其有效性 |
|no-store |无| 不缓存请求或响应的任何内容|
|no-transform |无| 代理不可更改媒体类型|
|must-revalidate| 无| 可缓存但必须再向源服务器进行确认|
|proxy-revalidate |无 |要求中间缓存服务器对缓存的响应有效性再 进行确认 |
|max-age = [ 秒] |必需| 响应的最大Age值 |
|s-maxage = [ 秒] |必需| 公共缓存服务器响应的最大Age值|
|cache-extension |-| 新指令标记（token）|

## 五、具体应用

### 5.1 连接管理

#### 1.长连接与短连接

&nbsp;&nbsp;&nbsp;&nbsp;当浏览器访问一个包含多张图片的 HTML 页面时，除了请求访问的 HTML 页面资源，还会请求图片资源。如果每进行一次 HTTP 通信就要新建一个 TCP 连接，那么开销会很大。

&nbsp;&nbsp;&nbsp;&nbsp;长连接只需要建立一次 TCP 连接就能进行多次 HTTP 通信。

- 从 HTTP/1.1 开始默认是长连接的，如果要断开连接，需要由客户端或者服务器端提出断开，使用Connection : close ；
-  在 HTTP/1.1 之前默认是短连接的，如果需要使用长连接，则使用 Connection : Keep-Alive 。

#### **2.** **流水线**

&nbsp;&nbsp;&nbsp;&nbsp;默认情况下，HTTP 请求是按顺序发出的，下一个请求只有在当前请求收到响应之后才会被发出。由于受到网络延迟和带宽的限制，在下一个请求被发送到服务器之前，可能需要等待很长时间。

&nbsp;&nbsp;&nbsp;&nbsp;流水线是在同一条长连接上连续发出请求，而不用等待响应返回，这样可以减少延迟。

### 5.2 **Cookie**

&nbsp;&nbsp;&nbsp;&nbsp;HTTP 协议是无状态的，主要是为了让 HTTP 协议尽可能简单，使得它能够处理大量事务。HTTP/1.1 引入 Cookie 来保存状态信息。

&nbsp;&nbsp;&nbsp;&nbsp;Cookie 是服务器发送到用户浏览器并保存在本地的一小块数据，它会在浏览器之后向同一服务器再次发起请求时被携带上，用于告知服务端两个请求是否来自同一浏览器。由于之后每次请求都会需要携带 Cookie 数据，因此会带来额外的性能开销（尤其是在移动环境下）。

&nbsp;&nbsp;&nbsp;&nbsp;Cookie 曾一度用于客户端数据的存储，因为当时并没有其它合适的存储办法而作为唯一的存储手段，但现在随着现代浏览器开始支持各种各样的存储方式，Cookie 渐渐被淘汰。新的浏览器 API 已经允许开发者直接将数据存储到本地，如使用 Web storage API（本地存储和会话存储）或 IndexedDB。

#### 用途

- 会话状态管理（如用户登录状态、购物车、游戏分数或其它需要记录的信息）
- 个性化设置（如用户自定义设置、主题等）
- 浏览器行为跟踪（如跟踪分析用户行为等）

#### **2.** **创建过程**

&nbsp;&nbsp;&nbsp;&nbsp;服务器发送的响应报文包含 Set-Cookie 首部字段，客户端得到响应报文后把 Cookie 内容保存到浏览器中

&nbsp;&nbsp;&nbsp;&nbsp;客户端之后对同一个服务器发送请求时，会从浏览器中取出 Cookie 信息并通过 Cookie 请求首部字段发送给服务器。

#### **3.** **分类**

- 会话期 Cookie：浏览器关闭之后它会被自动删除，也就是说它仅在会话期内有效。
- 持久性 Cookie：指定过期时间（Expires）或有效期（max-age）之后就成为了持久性的 Cookie。

#### **4. Session**

&nbsp;&nbsp;&nbsp;&nbsp;除了可以将用户信息通过 Cookie 存储在用户浏览器中，也可以利用 Session 存储在服务器端，存储在服务器端的信息更加安全。

&nbsp;&nbsp;&nbsp;&nbsp;Session 可以存储在服务器上的文件、数据库或者内存中。也可以将 Session 存储在 Redis 这种内存型数据库中，效率会更高。

&nbsp;&nbsp;&nbsp;&nbsp;使用 Session 维护用户登录状态的过程如下：

- 用户进行登录时，用户提交包含用户名和密码的表单，放入 HTTP 请求报文中；
- 服务器验证该用户名和密码，如果正确则把用户信息存储到 Redis 中，它在 Redis 中的 Key 称为 Session ID；
- 服务器返回的响应报文的 Set-Cookie 首部字段包含了这个 Session ID，客户端收到响应报文之后将该 Cookie值存入浏览器中；
- 客户端之后对同一个服务器进行请求时会包含该 Cookie 值，服务器收到之后提取出 Session ID，从 Redis 中取出用户信息，继续之前的业务操作。

&nbsp;&nbsp;&nbsp;&nbsp;应该注意 Session ID 的安全性问题，不能让它被恶意攻击者轻易获取，那么就不能产生一个容易被猜到的 SessionID 值。此外，还需要经常重新生成 Session ID。在对安全性要求极高的场景下，例如转账等操作，除了使用 Session管理用户状态之外，还需要对用户进行重新验证，比如重新输入密码，或者使用短信验证码等方式。

#### **5.** **浏览器禁用** **Cookie**

&nbsp;&nbsp;&nbsp;&nbsp;此时无法使用 Cookie 来保存用户信息，只能使用 Session。除此之外，不能再将 Session ID 存放到 Cookie 中，而是使用 URL 重写技术，将 Session ID 作为 URL 的参数进行传递。

#### 6.**Cookie** **与** **Session** **选择**

- Cookie 只能存储 ASCII 码字符串，而 Session 则可以存储任何类型的数据，因此在考虑数据复杂性时首选Session；
- Cookie 存储在浏览器中，容易被恶意查看。如果非要将一些隐私数据存在 Cookie 中，可以将 Cookie 值进行加密，然后在服务器进行解密；
- 对于大型网站，如果用户所有的信息都存储在 Session 中，那么开销是非常大的，因此不建议将所有的用户信息都存储到 Session 中。

### 5.3 缓存

#### 1.优点

- 缓解服务器压力；
- 降低客户端获取资源的延迟：缓存通常位于内存中，读取缓存的速度更快。并且缓存服务器在地理位置上也有 可能比源服务器来得近，例如浏览器缓存

#### 2.实现方式

- 让代理服务器进行缓存
- 让客户端浏览器进行缓存

#### 3. **Cache-Control**

&nbsp;&nbsp;&nbsp;&nbsp;HTTP/1.1 通过 Cache-Control 首部字段来控制缓存。具体的方法在上面通用首部已经写出，这里不再赘述。

### 5.4 内容协商

&nbsp;&nbsp;&nbsp;&nbsp;通过内容协商返回最合适的内容，例如根据浏览器的默认语言选择返回中文界面还是英文界面。

#### **1.** **类型**

**1.1** **服务端驱动型**

&nbsp;&nbsp;&nbsp;&nbsp;客户端设置特定的 HTTP 首部字段，例如 Accept、Accept-Charset、Accept-Encoding、Accept-Language，服务器根据这些字段返回特定的资源。

&nbsp;&nbsp;&nbsp;&nbsp;它存在以下问题：

- 服务器很难知道客户端浏览器的全部信息；
- 客户端提供的信息相当冗长（HTTP/2 协议的首部压缩机制缓解了这个问题），并且存在隐私风险（HTTP 指纹识别技术）；
- 给定的资源需要返回不同的展现形式，共享缓存的效率会降低，而服务器端的实现会越来越复杂。

**1.2** **代理驱动型**

&nbsp;&nbsp;&nbsp;&nbsp;服务器返回 300 Multiple Choices 或者 406 Not Acceptable，客户端从中选出最合适的那个资源。

#### **2. Vary**

`Vary: Accept-Language`

&nbsp;&nbsp;&nbsp;&nbsp;在使用内容协商的情况下，只有当缓存服务器中的缓存满足内容协商条件时，才能使用该缓存，否则应该向源服务器请求该资源。

&nbsp;&nbsp;&nbsp;&nbsp;例如，一个客户端发送了一个包含 Accept-Language 首部字段的请求之后，源服务器返回的响应包含 Vary: Accept-Language 内容，缓存服务器对这个响应进行缓存之后，在客户端下一次访问同一个 URL 资源，并且Accept-Language 与缓存中的对应的值相同时才会返回该缓存。

### 5.5 通信数据转发

#### 代理

&nbsp;&nbsp;&nbsp;&nbsp;代理服务器接受客户端的请求，并且转发给其它服务器。

&nbsp;&nbsp;&nbsp;&nbsp;使用代理的主要目的是：

- 缓存
- 负载均衡
- 网络访问控制
- 访问日志记录

&nbsp;&nbsp;&nbsp;&nbsp;代理服务器分为正向代理和反向代理两种：

- 用户察觉得到正向代理的存在。
- 而反向代理一般位于内部网络中，用户察觉不到。

#### 网关

&nbsp;&nbsp;&nbsp;&nbsp;与代理服务器不同的是，网关服务器会将 HTTP 转化为其它协议进行通信，从而请求其它非 HTTP 服务器的服务。

#### 隧道

&nbsp;&nbsp;&nbsp;&nbsp;使用 SSL 等加密手段，在客户端和服务器之间建立一条安全的通信线路。

## 六、HTTPS

HTTP 有以下安全性问题：

- 使用明文进行通信，内容可能会被窃听；
- 不验证通信方的身份，通信方的身份有可能遭遇伪装；
- 无法证明报文的完整性，报文有可能遭篡改。

&nbsp;&nbsp;&nbsp;&nbsp;HTTPS 并不是新协议，而是让 HTTP 先和 SSL（Secure Sockets Layer）通信，再由 SSL 和 TCP 通信，也就是说HTTPS 使用了隧道进行通信。

&nbsp;&nbsp;&nbsp;&nbsp;通过使用 SSL，HTTPS 具有了加密（防窃听）、认证（防伪装）和完整性保护（防篡改）。

### 加密

#### 对称加密

对称密钥加密（Symmetric-Key Encryption），加密和解密使用同一密钥。

- 优点：运算速度快；
- 缺点：无法安全地将密钥传输给通信方。

#### **非对称密钥加密**

非对称密钥加密，又称**公开密钥加密**（Public-Key Encryption），加密和解密使用不同的密钥。

&nbsp;&nbsp;&nbsp;&nbsp;公开密钥所有人都可以获得，通信发送方获得接收方的公开密钥之后，就可以使用公开密钥进行加密，接收方收到通信内容后使用私有密钥解密。

&nbsp;&nbsp;&nbsp;&nbsp;非对称密钥除了用来加密，还可以用来进行签名。因为私有密钥无法被其他人获取，因此通信发送方使用其私有密钥进行签名，通信接收方使用发送方的公开密钥对签名进行解密，就能判断这个签名是否正确。

- 优点：可以更安全地将公开密钥传输给通信发送方；
- 缺点：运算速度慢。

#### **HTTPS** **采用的加密方式**

HTTPS 采用混合的加密机制，使用非对称密钥加密用于传输对称密钥来保证传输过程的安全性，之后使用对称密钥加密进行通信来保证通信过程的效率。

## 七、**HTTP/1.1** **新特性**

详细内容请见上文

- 默认是长连接
- 支持流水线
- 支持同时打开多个 TCP 连接
- 支持虚拟主机
- 新增状态码 100
- 支持分块传输编码
- 新增缓存处理指令 max-age

## 八、**GET** **和** **POST** **比较**

### 8.1 作用

GET 用于获取资源，而 POST 用于传输实体主体

### 8.2 参数

GET 和 POST 的请求都能使用额外的参数，但是 GET 的参数是以查询字符串出现在 URL 中，而 POST 的参数存储在实体主体中。不能因为 POST 参数存储在实体主体中就认为它的安全性更高，因为照样可以通过一些抓包工具（Fiddler）查看。

&nbsp;&nbsp;&nbsp;&nbsp;因为 URL 只支持 ASCII 码，因此 GET 的参数中如果存在中文等字符就需要先进行编码。例如 中文 会转换为 %E4%B8%AD%E6%96%87 ，而空格会转换为 %20 。POST 参数支持标准字符集。

### 8.3 安全

安全的 HTTP 方法不会改变服务器状态，也就是说它只是可读的。

&nbsp;&nbsp;&nbsp;&nbsp;GET 方法是安全的，而 POST 却不是，因为 POST 的目的是传送实体主体内容，这个内容可能是用户上传的表单数据，上传成功之后，服务器可能把这个数据存储到数据库中，因此状态也就发生了改变。

- 安全的方法除了 GET 之外还有：HEAD、OPTIONS。
- 不安全的方法除了 POST 之外还有 PUT、DELETE。

### 8.4 幂等性

&nbsp;&nbsp;&nbsp;&nbsp;幂等的 HTTP 方法，同样的请求被执行一次与连续执行多次的效果是一样的，服务器的状态也是一样的。换句话说就是，幂等方法不应该具有副作用（统计用途除外）。

&nbsp;&nbsp;&nbsp;&nbsp;所有的安全方法也都是幂等的。

&nbsp;&nbsp;&nbsp;&nbsp;在正确实现的条件下，GET，HEAD，PUT 和 DELETE 等方法都是幂等的，而 POST 方法不是。

&nbsp;&nbsp;&nbsp;&nbsp;GET /pageX HTTP/1.1 是幂等的，连续调用多次，客户端接收到的结果都是一样的：

### 8.5 可缓性

如果要对响应进行缓存，需要满足以下条件：

- 请求报文的 HTTP 方法本身是可缓存的，包括 GET 和 HEAD，但是 PUT 和 DELETE 不可缓存，POST 在多数情况下不可缓存的。
- 响应报文的状态码是可缓存的，包括：200, 203, 204, 206, 300, 301, 404, 405, 410, 414, and 501。
- 响应报文的 Cache-Control 首部字段没有指定不进行缓存。