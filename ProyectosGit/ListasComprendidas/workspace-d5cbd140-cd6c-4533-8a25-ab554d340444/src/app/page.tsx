"use client";

import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { CheckCircle, XCircle, Lightbulb, Code, Trophy } from "lucide-react";

interface QuizQuestion {
  id: number;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
}

export default function PythonListComprehensions() {
  const [quizAnswers, setQuizAnswers] = useState<{[key: number]: number}>({});
  const [showResults, setShowResults] = useState<{[key: number]: boolean}>({});
  const [codeInput, setCodeInput] = useState("");
  const [codeResult, setCodeResult] = useState("");

  const quizQuestions: QuizQuestion[] = [
    {
      id: 1,
      question: "¿Qué produce esta lista comprendida: [x*2 for x in range(5)]?",
      options: ["[0, 2, 4, 6, 8]", "[2, 4, 6, 8, 10]", "[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]"],
      correctAnswer: 0,
      explanation: "range(5) produce [0, 1, 2, 3, 4] y cada elemento se multiplica por 2 usando la lista comprendida."
    },
    {
      id: 2,
      question: "¿Cuál es la forma correcta de crear una lista con los cuadrados de los números pares del 0 al 10 usando una lista comprendida?",
      options: ["[x**2 for x in range(11) if x % 2 == 0]", "[x for x in range(11) if x % 2 == 0]", "[x**2 for x in range(11)]", "[x*2 for x in range(6)]"],
      correctAnswer: 0,
      explanation: "La primera opción usa una lista comprendida con condición para filtrar números pares y luego elevarlos al cuadrado."
    },
    {
      id: 3,
      question: "¿Qué produce esta lista comprendida anidada: [(x, y) for x in [1, 2] for y in ['a', 'b']]?",
      options: ["[(1, 'a'), (2, 'b')]", "[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]", "[(1, 2), ('a', 'b')]", "[(1, 'a', 'b'), (2, 'a', 'b')]"],
      correctAnswer: 1,
      explanation: "Es una lista comprendida anidada que crea todas las combinaciones posibles entre los elementos de las dos listas."
    }
  ];

  const handleQuizAnswer = (questionId: number, answerIndex: number) => {
    setQuizAnswers(prev => ({ ...prev, [questionId]: answerIndex }));
    setShowResults(prev => ({ ...prev, [questionId]: true }));
  };

  const isCorrect = (questionId: number) => {
    return quizAnswers[questionId] === quizQuestions.find(q => q.id === questionId)?.correctAnswer;
  };

  const examples = [
    {
      title: "Básica",
      code: "[x**2 for x in range(10)]",
      description: "Crea una lista con los cuadrados del 0 al 9 usando lista comprendida",
      result: "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
    },
    {
      title: "Con condición",
      code: "[x for x in range(20) if x % 2 == 0]",
      description: "Lista comprendida que filtra solo números pares",
      result: "[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]"
    },
    {
      title: "Con transformación y condición",
      code: "[x**2 for x in range(10) if x % 2 == 1]",
      description: "Lista comprendida con cuadrados de solo números impares",
      result: "[1, 9, 25, 49, 81]"
    },
    {
      title: "Anidada",
      code: "[(x, y) for x in [1, 2, 3] for y in ['a', 'b']]",
      description: "Lista comprendida anidada que crea combinaciones",
      result: "[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]"
    },
    {
      title: "Con if-else",
      code: "[x**2 if x % 2 == 0 else x**3 for x in range(5)]",
      description: "Lista comprendida con diferentes transformaciones según condición",
      result: "[0, 1, 4, 27, 16]"
    },
    {
      title: "Con strings",
      code: "[palabra.upper() for palabra in ['hola', 'mundo', 'python']]",
      description: "Lista comprendida aplicando método a strings",
      result: "['HOLA', 'MUNDO', 'PYTHON']"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-blue-100 p-4">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center py-8">
          <h1 className="text-4xl md:text-6xl font-bold text-blue-900 mb-4">
            Listas Comprendidas en Python
          </h1>
          <p className="text-xl text-blue-700 max-w-3xl mx-auto">
            Aprende a crear listas de manera elegante y eficiente con Python
          </p>
          <p className="text-lg text-blue-600 mt-2">
            Por Victor Cordoba
          </p>
          <div className="flex justify-center mt-4">
            <Badge className="bg-yellow-400 text-blue-900 text-lg px-4 py-2">
              <Code className="w-5 h-5 mr-2" />
              Python Intermedio
            </Badge>
          </div>
        </div>

        {/* Introduction */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle className="flex items-center gap-2">
              <Lightbulb className="w-6 h-6" />
              ¿Qué son las Listas Comprendidas?
            </CardTitle>
          </CardHeader>
          <CardContent className="p-6">
            <p className="text-lg text-gray-700 mb-4">
              Las <strong className="text-blue-600">listas comprendidas</strong> (list comprehensions) son una característica 
              elegante de Python que permite crear listas de manera concisa y legible en una sola línea de código.
            </p>
            <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded mb-4">
              <p className="text-blue-800">
                <strong>Sintaxis básica:</strong> <code className="bg-blue-100 px-2 py-1 rounded">[expresión for item in iterable]</code>
              </p>
            </div>
            <div className="space-y-4">
              <h3 className="text-xl font-bold text-blue-900">Ventajas sobre los bucles tradicionales:</h3>
              <ul className="space-y-2 text-gray-700">
                <li className="flex items-start gap-2">
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span><strong>Concisión:</strong> Reducen múltiples líneas a una sola expresión clara</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span><strong>Rendimiento:</strong> Generalmente son más rápidas que los bucles for equivalentes</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span><strong>Legibilidad:</strong> Una vez aprendidas, son más fáciles de leer y entender</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span><strong>Estilo Pythonico:</strong> Siguen la filosofía de Python de código limpio y expresivo</span>
                </li>
              </ul>
            </div>
            <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
              <h4 className="font-bold text-yellow-800 mb-2">Comparación con bucles tradicionales:</h4>
              <div className="grid md:grid-cols-2 gap-4">
                <div>
                  <p className="text-sm font-semibold text-gray-700 mb-1">Bucle tradicional:</p>
                  <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm">
                    {`cuadrados = []\nfor x in range(10):\n    cuadrados.append(x**2)`}
                  </div>
                </div>
                <div>
                  <p className="text-sm font-semibold text-gray-700 mb-1">Lista comprendida:</p>
                  <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm">
                    {`cuadrados = [x**2 for x in range(10)]`}
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Theory Section */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle>Teoría Avanzada</CardTitle>
            <CardDescription className="text-blue-100">
              Profundiza en los conceptos fundamentales de las listas comprendidas
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="space-y-6">
              <div>
                <h3 className="text-xl font-bold text-blue-900 mb-3">Sintaxis Completa</h3>
                <div className="bg-blue-50 p-4 rounded-lg">
                  <code className="text-blue-800 font-mono text-lg">
                    [expresión for item in iterable if condición]
                  </code>
                </div>
                <p className="text-gray-700 mt-3">
                  La sintaxis completa incluye una parte opcional de filtrado con <code className="bg-blue-100 px-1 rounded">if</code>.
                </p>
              </div>

              <div>
                <h3 className="text-xl font-bold text-blue-900 mb-3">Tipos de Listas Comprendidas</h3>
                <div className="grid md:grid-cols-2 gap-4">
                  <Card className="border-yellow-200 bg-yellow-50">
                    <CardHeader className="bg-yellow-400 text-blue-900">
                      <CardTitle className="text-lg">Simple</CardTitle>
                    </CardHeader>
                    <CardContent className="p-4">
                      <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm mb-2">
                        [x**2 for x in range(5)]
                      </div>
                      <p className="text-sm text-gray-700">
                        Transforma cada elemento sin filtrado
                      </p>
                    </CardContent>
                  </Card>

                  <Card className="border-yellow-200 bg-yellow-50">
                    <CardHeader className="bg-yellow-400 text-blue-900">
                      <CardTitle className="text-lg">Condicional</CardTitle>
                    </CardHeader>
                    <CardContent className="p-4">
                      <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm mb-2">
                        [x**2 for x in range(10) if x % 2 == 0]
                      </div>
                      <p className="text-sm text-gray-700">
                        Filtra elementos antes de transformarlos
                      </p>
                    </CardContent>
                  </Card>

                  <Card className="border-yellow-200 bg-yellow-50">
                    <CardHeader className="bg-yellow-400 text-blue-900">
                      <CardTitle className="text-lg">Anidada</CardTitle>
                    </CardHeader>
                    <CardContent className="p-4">
                      <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm mb-2">
                        [(x,y) for x in [1,2] for y in ['a','b']]
                      </div>
                      <p className="text-sm text-gray-700">
                        Crea combinaciones de múltiples iterables
                      </p>
                    </CardContent>
                  </Card>

                  <Card className="border-yellow-200 bg-yellow-50">
                    <CardHeader className="bg-yellow-400 text-blue-900">
                      <CardTitle className="text-lg">Con if-else</CardTitle>
                    </CardHeader>
                    <CardContent className="p-4">
                      <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm mb-2">
                        [x**2 if x%2==0 else x**3 for x in range(5)]
                      </div>
                      <p className="text-sm text-gray-700">
                        Aplica diferentes transformaciones según condición
                      </p>
                    </CardContent>
                  </Card>
                </div>
              </div>

              <div>
                <h3 className="text-xl font-bold text-blue-900 mb-3">Buenas Prácticas</h3>
                <div className="bg-green-50 border-l-4 border-green-500 p-4 rounded">
                  <ul className="space-y-2 text-gray-700">
                    <li className="flex items-start gap-2">
                      <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                      <span><strong>Mantén la simplicidad:</strong> Si la lista comprendida se vuelve muy compleja, considera usar un bucle for tradicional</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                      <span><strong>Nombres descriptivos:</strong> Usa nombres de variables claros aunque sean breves</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                      <span><strong>Evita efectos secundarios:</strong> Las listas comprendidas deben ser puras, sin modificar variables externas</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                      <span><strong>Rendimiento:</strong> Son excelentes para operaciones matemáticas y transformaciones de datos</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Examples */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle>Ejemplos Prácticos</CardTitle>
            <CardDescription className="text-blue-100">
              Explora diferentes tipos de listas comprendidas con ejemplos ejecutables
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {examples.map((example, index) => (
                <Card key={index} className="border-yellow-300 bg-yellow-50">
                  <CardHeader className="bg-yellow-400 text-blue-900">
                    <CardTitle className="text-lg">{example.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="p-4 space-y-3">
                    <div className="bg-gray-900 text-green-400 p-3 rounded font-mono text-sm">
                      {example.code}
                    </div>
                    <p className="text-gray-700 text-sm">{example.description}</p>
                    <div className="bg-blue-100 p-3 rounded">
                      <p className="text-sm text-blue-800"><strong>Resultado:</strong></p>
                      <p className="font-mono text-blue-900 text-sm">{example.result}</p>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Interactive Quiz */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle className="flex items-center gap-2">
              <Trophy className="w-6 h-6" />
              Quiz Sorpresa
            </CardTitle>
            <CardDescription className="text-blue-100">
              Pon a prueba tus conocimientos con estos quizzes interactivos
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="space-y-6">
              {quizQuestions.map((question) => (
                <Card key={question.id} className="border-yellow-200">
                  <CardHeader className="bg-yellow-100">
                    <CardTitle className="text-lg text-blue-900">
                      Pregunta {question.id}
                    </CardTitle>
                    <CardDescription className="text-blue-700">
                      {question.question}
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="p-4">
                    <div className="space-y-3">
                      {question.options.map((option, index) => (
                        <Button
                          key={index}
                          variant={quizAnswers[question.id] === index ? "default" : "outline"}
                          className={`w-full text-left justify-start ${
                            quizAnswers[question.id] === index 
                              ? isCorrect(question.id) 
                                ? "bg-green-500 hover:bg-green-600" 
                                : "bg-red-500 hover:bg-red-600"
                              : "hover:bg-yellow-100"
                          }`}
                          onClick={() => handleQuizAnswer(question.id, index)}
                          disabled={showResults[question.id]}
                        >
                          {option}
                        </Button>
                      ))}
                    </div>
                    {showResults[question.id] && (
                      <Alert className={`mt-4 ${isCorrect(question.id) ? "border-green-500 bg-green-50" : "border-red-500 bg-red-50"}`}>
                        <div className="flex items-center gap-2">
                          {isCorrect(question.id) ? (
                            <CheckCircle className="w-5 h-5 text-green-600" />
                          ) : (
                            <XCircle className="w-5 h-5 text-red-600" />
                          )}
                          <AlertDescription className={isCorrect(question.id) ? "text-green-800" : "text-red-800"}>
                            {question.explanation}
                          </AlertDescription>
                        </div>
                      </Alert>
                    )}
                  </CardContent>
                </Card>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Practice Area */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle>Área de Práctica</CardTitle>
            <CardDescription className="text-blue-100">
              Escribe tus propias listas comprendidas y ve los resultados
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Escribe una lista comprendida:
                </label>
                <Input
                  placeholder="[x**2 for x in range(5)]"
                  value={codeInput}
                  onChange={(e) => setCodeInput(e.target.value)}
                  className="font-mono"
                />
              </div>
              <Button 
                onClick={() => {
                  try {
                    // Simulación de evaluación (en un entorno real esto requeriría un backend seguro)
                    if (codeInput.includes("[") && codeInput.includes("]")) {
                      setCodeResult("¡Buena sintaxis! En un entorno real, esto ejecutaría tu código Python.");
                    } else {
                      setCodeResult("Asegúrate de usar la sintaxis correcta de lista comprendida.");
                    }
                  } catch (error) {
                    setCodeResult("Error en el código. Revisa la sintaxis.");
                  }
                }}
                className="bg-yellow-400 hover:bg-yellow-500 text-blue-900"
              >
                Ejecutar Código
              </Button>
              {codeResult && (
                <Alert className="border-blue-300 bg-blue-50">
                  <AlertDescription className="text-blue-800">
                    {codeResult}
                  </AlertDescription>
                </Alert>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Summary */}
        <Card className="border-blue-300 bg-white shadow-lg">
          <CardHeader className="bg-blue-600 text-white">
            <CardTitle>Resumen</CardTitle>
          </CardHeader>
          <CardContent className="p-6">
            <div className="grid md:grid-cols-2 gap-6">
              <div className="space-y-3">
                <h3 className="text-xl font-bold text-blue-900">Ventajas</h3>
                <ul className="space-y-2 text-gray-700">
                  <li className="flex items-center gap-2">
                    <CheckCircle className="w-5 h-5 text-green-500" />
                    Código más conciso y legible
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="w-5 h-5 text-green-500" />
                    Mejor rendimiento que bucles tradicionales
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle className="w-5 h-5 text-green-500" />
                    Sintaxis elegante y pythonica
                  </li>
                </ul>
              </div>
              <div className="space-y-3">
                <h3 className="text-xl font-bold text-blue-900">Casos de Uso</h3>
                <ul className="space-y-2 text-gray-700">
                  <li>• Transformación de datos</li>
                  <li>• Filtrado de elementos</li>
                  <li>• Creación de combinaciones</li>
                  <li>• Procesamiento matemático</li>
                </ul>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}