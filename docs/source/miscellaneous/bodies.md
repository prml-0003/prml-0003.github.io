
# Listed Bodies

## The Listed Bodies

The listed bodies that <a href="https://www.legislation.gov.uk/ssi/2015/347/contents/made" target="_blank">Climate Change (Scotland) Order 2015</a>, and its <a href="https://www.legislation.gov.uk/ssi/2020/281/contents/made" target="_blank">amendment</a>.  Include

<ul class="disc">
  <li class="disc">Ministers, The Parliament</li>
  <li class="disc">Holders of offices in the Scottish Administration which are non-ministerial offices</li>
  <li class="disc">Local Government</li>
  <li class="disc">National Health Service</li>
  <li class="disc">Educational Institutions</li>
  <li class="disc">Police</li>
  <li class="disc">Others</li>
</ul>

<br>

**A plausible set of attributes** in a table named **bodies** is

<table style="width: 95%; margin-left: 35px; font-size: 95%">
    <colgroup>
        <col span="1" style="width: 13.5%;">
        <col span="1" style="width: 11.5%;">
        <col span="1" style="width: 60.0%;">
    </colgroup>
    <thead><tr style="text-align: left">
        <th>field</th><th>unit of<br>measure</th><th>notes</th></tr>
    </thead>
    <tr><td>body_name</td>
        <td>unitless</td><td>Scottish Ambulance Service Board</td></tr>
    <tr><td>body_id</td>
        <td>nominal number</td><td>A body's unique identification code, e.g., 3999131.</td></tr>
    <tr><td>body_type_id</td>
        <td>nominal number</td><td>The unique identification code of a body type; enables linking to a table of body types.</td></tr>
</table>

<br>

Each instance of the bodies should represent a distinct body.  In addition to the order's explicitly named bodies, ensure that the inventory of bodies includes

<ul class="disc">
<li class="disc">Local Government Bodies</li>
  <ul class="circle">
    <li class="circle"><a href="https://www.mygov.scot/organisations#scottish-local-authority" target="_blank">32 local authorities</a></li>
    <li class="circle"><a href="https://www.transport.gov.scot/our-approach/strategy/regional-transport-partnerships/" target="_blank">7 regional transport partnerships</a></li>
  </ul>  
<li class="disc">Educational Institutions</li>
<li class="disc">Others</li>
    <ul class="circle"><li class="circle">Integration Joint Boards: REF. <a href="https://www.legislation.gov.uk/asp/2014/9/section/9" target="_blank">9.2</a> of  <a href="https://www.legislation.gov.uk/asp/2014/9/contents">Public Bodies (Joint Working) (Scotland) Act 2014</a></li></ul>
</ul>

<br>

## The Listed Bodies: Scotland's National Health Service

A body type may have its own classifications, e.g., Scotland's National Health Service organisations fall into one of the following health body classes

<ul class="disc">
  <li class="disc">Regional</li>
  <li class="disc">Special</li>
  <li class="disc">Public</li>
</ul>

Consequently, the aforementioned **bodies** table might be expanded.  The **plausible set of attributes** being

<table style="width: 95%; margin-left: 35px; font-size: 95%">
    <colgroup>
        <col span="1" style="width: 13.5%;">
        <col span="1" style="width: 11.5%;">
        <col span="1" style="width: 60.0%;">
    </colgroup>
    <thead><tr style="text-align: left">
        <th>field</th><th>unit of<br>measure</th><th>notes</th></tr>
    </thead>
    <tr><td>body_name</td>
        <td>unitless</td><td>Scottish Ambulance Service Board</td></tr>
    <tr><td>body_id</td>
        <td>nominal number</td><td>A body's unique identification code, e.g., 3999131.</td></tr>
    <tr><td>body_type_id</td>
        <td>nominal number</td><td>The unique identification code of a body type, e.g., 6113 for National Health Service bodies; enables linking to a table of body types.</td></tr>
    <tr><td>body_type_class_id</td>
        <td>nominal number</td><td>The unique identification code of a body type class, e.g., 1 for <b>regional</b> national health service bodey; enables linking to a table of body type classes.</td></tr>
</table>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
