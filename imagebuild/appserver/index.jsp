<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>mariadb jdbc connect test</title>
</head>
<body>
 
<%
Connection conn = null;
String url = "jdbc:mariadb://172.18.0.4:3306/sample";
String id = "root";                     //MySQL에 접속을 위한 계정의 ID
String pwd = "qwer";            //MySQL에 접속을 위한 계정의 암호
Class.forName("org.mariadb.jdbc.Driver");
conn = DriverManager.getConnection(url, id, pwd);
out.println("<h1>MariaDB DB 연결 완료 </h1>");
%>
 
</body>
 
</html>
