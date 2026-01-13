<!DOCTYPE html>
<html lang="en">
<head>
<!--
"Time-stamp: <Sat, 01-02-21, 19:38:14 Eastern Standard Time>"
//-->
<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="My online portfolio that illustrates skills acquired while working through various project requirements.">
	<meta name="author" content="Julia Sveen">
	<link rel="icon" href="favicon.ico">

	<title>LIS4368 - Assignment2</title>

	<%@ include file="/css/include_css.jsp" %>		
	
</head>
<body>

<!-- display application path -->
<% //= request.getContextPath()%>
	
<!-- can also find path like this...<a href="${pageContext.request.contextPath}${'/a5/index.jsp'}">A5</a> -->

	<%@ include file="/global/nav.jsp" %>	

	<div class="container">
		<div class="starter-template">
					<div class="page-header">
						<%@ include file="global/header.jsp" %>
					</div>

					<b>http://localhost:9999/hello & http://localhost:9999/hello/index.html</b><br />
					<img src="img/helloindex.png" class="img-responsive center-block" alt="Using Servlets" />

					<br /> <br />
					<b>http://localhost:9999/hello/sayhello</b><br />
					<img src="img/sayhello.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>http://localhost:9999/hello/querybook.html</b><br />
					<img src="img/querybook.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>query results </b><br />
					<img src="img/queryresults.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>a2 index </b><br />
					<img src="img/a2index.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>ss1 </b><br /><br />
					<img src="img/ss1.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>ss2 </b><br />
					<img src="img/ss2.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
					<br />
					<b>ss3 </b><br /><br />
					<img src="img/ss3.png" class="img-responsive center-block" alt="Database Connectivity Using Servlets" />
	<%@ include file="/global/footer.jsp" %>

	</div> <!-- end starter-template -->
 </div> <!-- end container -->

 	<%@ include file="/js/include_js.jsp" %>		

</body>
</html>
