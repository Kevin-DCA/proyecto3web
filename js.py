#!C:/Users/leoviquez/AppData/Local/Programs/Python/Python37-32/python.exe
print ("Content-type: text/javascript\n\n")

print (
    """
function login()
        {
            console.log("init login");
            xhr= new XMLHttpRequest();
            usuario=document.getElementById("usuario").value;
            clave=document.getElementById("clave").value;
            url="./login.py";
            parametros=`usuario=${usuario}&clave=${clave}`;
            xhr.open("POST",url);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.onload= function ()
            {
                div=document.getElementById("respuesta");
                div.innerHTML=xhr.responseText;
            };
            xhr.send(parametros);
        }

        var lista_personas=[];
        function personas()
        {
            xhr= new XMLHttpRequest();
            url="./personas.py";
            xhr.open("GET",url);
            xhr.onload= function ()
            {
                lista_personas=eval(xhr.responseText);
                imprimatabla(lista_personas);
            };
            xhr.send();
        }
        function imprimatabla(l)
        {
            table=document.createElement("table");
            
            for (var i in l)
            {
                fila=document.createElement("tr");
                table.appendChild (fila);
                id=document.createElement("td");
                id.innerHTML=l[i].id;
                fila.appendChild(id);
                nombre=document.createElement("td");
                nombre.innerHTML=l[i].nombre;
                fila.appendChild(nombre);
                apellido1=document.createElement("td");
                apellido1.innerHTML=l[i].apellido1;
                fila.appendChild(apellido1);
                apellido2=document.createElement("td");
                apellido2.innerHTML=l[i].apellido2;
                fila.appendChild(apellido2);
            }
            document.getElementById("contenedor_personas").appendChild(table);
        }

    """
)

        