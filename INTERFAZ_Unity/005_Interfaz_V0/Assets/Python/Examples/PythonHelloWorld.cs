using UnityEngine;
using IronPython.Hosting;

namespace Exodrifter.UnityPython.Examples
{
	public class PythonHelloWorld : MonoBehaviour
	{
		void Start()
		{
			var engine = Python.CreateEngine();
			var scope = engine.CreateScope();

			string code = "str = 'Hello world!'\n"+
							"str2= 'Hola Juan'\n" +
							"suma = 5+2";

			var source = engine.CreateScriptSourceFromString(code);
			source.Execute(scope);

			Debug.Log(scope.GetVariable<int>("suma"));
		}
	}
}