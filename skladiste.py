from flask import Flask, redirect, url_for, render_template, request, flash, request
import dbOperacije as dbo

app=Flask(__name__)

@app.route("/")
@app.route("/Main.html")
def mainPage():
	return render_template('Main.html')

@app.route("/DodajProizvod.html", methods=["POST", "GET"])
def dodajProizvod():
	if request.method == "POST":
		pName = request.form["pname"]
		pPrice = float(request.form["pprice"])
		pAmount = int(request.form["pamount"])
		add_new = dbo.dodajProizvod(pName,pPrice,pAmount)
		return redirect(url_for('dodajProizvod'))
	else:
		return render_template('DodajProizvod.html')

@app.route("/DodajKupca.html", methods=["POST", "GET"])
def dodajKupca():
	if request.method == "POST":
		cfName = request.form["fname"]
		clName = request.form["lname"]
		cStreet = request.form["cstreet"]
		cPostCode = int(request.form["cpostcode"])
		cAge = int(request.form["cage"])
		add_new = dbo.dodajKupca(cfName,clName,cStreet,cPostCode,cAge)
		return redirect(url_for('dodajKupca'))
	else:
		return render_template('DodajKupca.html')
	
@app.route("/DodajOsoblje.html", methods=["POST", "GET"])
def dodajOsoblje():
	if request.method == "POST":
		sfName = request.form["fname"]
		slName = request.form["lname"]
		sEmployeeSince = request.form["semployeesince"]
		sAge = int(request.form["sage"])
		add_new = dbo.dodajOsoblje(sfName,slName,sEmployeeSince,sAge)
		return redirect(url_for('dodajOsoblje'))
	else:
		return render_template('DodajOsoblje.html')

@app.route("/DodajPorudzbinu.html")
def fillCombo():
	product_list=dbo.prikaziProizvod()
	customer_list=dbo.prikaziKupca()
	staff_list=dbo.prikaziOsoblje()
	return render_template('DodajPorudzbinu.html', product_list=product_list,customer_list=customer_list,staff_list=staff_list)

@app.route("/DodajPorudzbinu.html", methods=["POST", "GET"])
def dodajPorudzbinu():
	if request.method == "POST":
		opid = int(request.form["ProductSelect"])
		ocid = int(request.form["CustomerSelect"])
		osid = int(request.form["StaffSelect"])
		ocount = int(request.form["pamount"])
		add_new = dbo.dodajPorudzbinu(opid, ocid, osid, ocount)
		return redirect(url_for('dodajPorudzbinu'))
	else:
		return render_template('DodajPorudzbinu.html')

@app.route("/PrikaziProizvod.html")
def prikaziProizvode():
	product_list=dbo.prikaziProizvod()
	return render_template('PrikaziProizvod.html', product_list=product_list)

@app.route("/PrikaziKupca.html")
def prikaziKupca():
	customer_list=dbo.prikaziKupca()
	return render_template("PrikaziKupca.html", customer_list=customer_list)

@app.route("/PrikaziOsoblje.html")
def prikaziOsoblje():
	staff_list=dbo.prikaziOsoblje()
	return render_template("PrikaziOsoblje.html", staff_list=staff_list)

@app.route("/PrikaziPorudzbinu.html")
def prikaziPorudzbinu():
	order_list=dbo.prikaziPorudzbinu()
	return render_template("PrikaziPorudzbinu.html", order_list=order_list)

@app.route("/IzbrisiProizvod.html")
def IzbrisiProizvodMain():
	product_list=dbo.prikaziProizvod()
	return render_template('IzbrisiProizvod.html', product_list=product_list)

@app.route("/IzbrisiProizvod.html/<int:pid>")
def izbrisiProizvodID(pid):
	if (request.args.get("submit") == "Submit"):
		dbo.IzbrisiTacanProizvod(int(pid))
		return redirect(url_for('IzbrisiProizvodMain'))
	else:
		exac_product=dbo.prikaziTacanProizvod(int(pid))
		return render_template('IzbrisiProizvod.html', exac_product=exac_product)

@app.route("/IzbrisiKupca.html")
def izbrisiKupcaMain():
  customer_list=dbo.prikaziKupca()
  return render_template('IzbrisiKupca.html', customer_list=customer_list)

@app.route("/IzbrisiKupca.html/<int:cid>")
def izbrisiKupcaID(cid):
  if (request.args.get("submit") == "Submit"):
    dbo.IzbrisiTacnogKupca(int(cid))
    return redirect(url_for('izbrisiKupcaMain'))
  else:
    exac_customer=dbo.PrikaziTacnogKupca(int(cid))
    return render_template('IzbrisiKupca.html', exac_customer=exac_customer)

@app.route("/IzbrisiOsoblje.html")
def izbrisiOsobljeMain():
  staff_list=dbo.prikaziOsoblje()
  return render_template('IzbrisiOsoblje.html', staff_list=staff_list)

@app.route("/IzbrisiOsoblje.html/<int:sid>")
def izbrisiOsobljeID(sid):
  if (request.args.get("submit") == "Submit"):
    dbo.IzbrisiTacnoOsoblje(int(sid))
    return redirect(url_for('izbrisiOsobljeMain'))
  else:
    exac_staff=dbo.PrikaziTacnoOsoblje(int(sid))
    return render_template('IzbrisiOsoblje.html', exac_staff=exac_staff)

@app.route("/IzbrisiPorudzbinu.html")
def izbrisiPorudzbinuMain():
  order_list=dbo.prikaziPorudzbinu()
  return render_template('IzbrisiPorudzbinu.html', order_list=order_list)

@app.route("/IzbrisiPorudzbinu.html/<int:oid>")
def izbrisiPorudzbinuID(oid):
  if (request.args.get("submit") == "Submit"):
    dbo.izbrisiTacnuPorudzbinu(int(oid))
    return redirect(url_for('izbrisiPorudzbinuMain'))
  else:
    exac_order=dbo.PrikaziTacnuPorudzbinu(int(oid))
    return render_template('IzbrisiPorudzbinu.html', exac_order=exac_order)

@app.route("/UrediProizvod.html")
def urediProizvodMain():
	product_list=dbo.prikaziProizvod()
	return render_template('UrediProizvod.html', product_list=product_list)

@app.route("/UrediProizvod.html/<int:pid1>", methods=["POST", "GET"])
def urediProizvodID(pid1):
	if request.method == "POST":
		pID = request.form["pid"]
		pName = request.form["pname"]
		pPrice = float(request.form["pprice"])
		pAmount = int(request.form["pamount"])
		edit_row = dbo.urediProizvod(pID,pName,pPrice,pAmount)
		return redirect(url_for('urediProizvodMain'))
	else:
		exac_product=dbo.prikaziTacanProizvod(int(pid1))
		product_list=exac_product
		return render_template('UrediProizvod.html', exac_product=exac_product, product_list=product_list)

@app.route("/UrediKupca.html")
def urediKupcaMain():
  Customer_list=dbo.prikaziKupca()
  return render_template('UrediKupca.html', Customer_list=Customer_list)

@app.route("/UrediKupca.html/<int:cid1>", methods=["POST", "GET"])
def urediKupcaID(cid1):
	if request.method == "POST":
		cID = int(request.form["cid"])
		fName = request.form["fname"]
		lName = request.form["lname"]
		cStreet = request.form["cstreet"]
		cPostCode = int(request.form["cpostcode"])
		cAge = int(request.form["cage"])
		edit_row = dbo.urediKupca(cID,fName,lName,cStreet,cPostCode,cAge)
		return redirect(url_for('urediKupcaMain'))
	else:
		exac_Customer=dbo.PrikaziTacnogKupca(int(cid1))
		Customer_list=exac_Customer
		return render_template('UrediKupca.html', exac_Customer=exac_Customer, Customer_list=Customer_list)

@app.route("/UrediOsoblje.html")
def urediOsobljeMain():
  Staff_list=dbo.prikaziOsoblje()
  return render_template('UrediOsoblje.html', Staff_list=Staff_list)

@app.route("/UrediOsoblje.html/<int:sid1>", methods=["POST", "GET"])
def urediOsobljeID(sid1):
	if request.method == "POST":
		sid = request.form["sid"]
		fName = request.form["fname"]
		lName = request.form["lname"]
		sEmployeeSince = request.form["semployeesince"]
		sAge = int(request.form["sage"])
		edit_row = dbo.urediOsoblje(sid,fName,lName,sEmployeeSince,sAge)
		return redirect(url_for('urediOsobljeMain'))
	else:
		exac_Staff=dbo.PrikaziTacnoOsoblje(int(sid1))
		Staff_list=exac_Staff
		return render_template('UrediOsoblje.html', exac_Staff=exac_Staff, Staff_list=Staff_list)

@app.route("/UrediPorudzbinu.html")
def urediPorudzbinuMain():
  Order_list=dbo.prikaziPorudzbinu()
  return render_template('UrediPorudzbinu.html', Order_list=Order_list)

@app.route("/UrediPorudzbinu.html/<int:oid1>", methods=["POST", "GET"])
def urediPorudzbinuID(oid1):
	if request.method == "POST":
		oid = int(request.form["oid"])
		productid = int(request.form["ProductSelect"])
		customerid = int(request.form["CustomerSelect"])
		staffid = int(request.form["StaffSelect"])
		ocount = int(request.form["ocount"])
		edit_row = dbo.urediPorudzbinu(oid,productid,customerid,staffid,ocount)
		return redirect(url_for('urediPorudzbinuMain'))
	else:
		product_list=dbo.prikaziProizvod()
		customer_list=dbo.prikaziKupca()
		staff_list=dbo.prikaziOsoblje()
		exac_Order=dbo.PrikaziTacnuPorudzbinu(int(oid1))
		Order_list=exac_Order
		return render_template('UrediPorudzbinu.html', exac_Order=exac_Order, Order_list=Order_list, product_list=product_list, customer_list=customer_list, staff_list=staff_list)

if __name__=='__main__':
	app.run(debug=True)