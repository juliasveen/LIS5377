<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Updated Meta Tags -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Customer management system - Add new customers securely and efficiently.">
    <meta name="author" content="Julia Sveen">
    <title>LIS4368 - Project1</title>
    <link rel="icon" href="favicon.ico">
    <%@ include file="/css/include_css.jsp" %>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.5/jquery.validate.min.js"></script>
    <link rel="stylesheet" href="/css/custom.css">
</head>
<body>
    <%@ include file="/global/nav.jsp" %>
    <div class="container">
        <div class="starter-template">
            <div class="page-header">
                <%@ include file="global/header.jsp" %>
            </div>
            <form id="add_customer_form" method="post" action="submit_customer.jsp" class="form-horizontal">
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_fname">FName:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_fname" name="cus_fname" class="form-control" required maxlength="30">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_lname">LName:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_lname" name="cus_lname" class="form-control" required maxlength="30">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_street">Street:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_street" name="cus_street" class="form-control" required maxlength="30">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_city">City:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_city" name="cus_city" class="form-control" required maxlength="30">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_state">State:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_state" name="cus_state" class="form-control" required pattern="[A-Za-z]{2}">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_zip">Zip Code:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_zip" name="cus_zip" class="form-control" required pattern="\d{5,9}">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_phone">Phone:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_phone" name="cus_phone" class="form-control" required pattern="\d{10}">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_email">Email:</label>
                    <div class="col-sm-4">
                        <input type="email" id="cus_email" name="cus_email" class="form-control" required>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_balance">Balance:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_balance" name="cus_balance" class="form-control" required pattern="\d{1,6}(\.\d{1,2})?">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_total_sales">Total Sales:</label>
                    <div class="col-sm-4">
                        <input type="text" id="cus_total_sales" name="cus_total_sales" class="form-control" required pattern="\d{1,6}(\.\d{1,2})?">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-4 control-label" for="cus_notes">Notes:</label>
                    <div class="col-sm-4">
                        <textarea id="cus_notes" name="cus_notes" class="form-control"></textarea>
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-sm-4 col-sm-offset-4">
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <script>
        $(document).ready(function() {
            $("#add_customer_form").validate();
        });
    </script>
</body>
</html>
