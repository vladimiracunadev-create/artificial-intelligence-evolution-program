# Evaluación — 183 Inferencia privada, computación confidencial y attestation

## ❓ Preguntas

1. Distingue cifrado en tránsito, en reposo y **en uso**.
2. Explica por qué una medición de runtime y una attestation no prueban que el modelo sea correcto.
3. Separa las garantías de un TEE de las de privacidad diferencial, aprendizaje federado y ZDR.
4. ¿Qué debe comprobar una política antes de liberar una clave a un entorno confidencial?
5. Propón dos ataques que queden fuera del perímetro de una attestation válida.

## 🏆 Reto verificable

Amplía el laboratorio con una tercera solicitud que tenga runtime aprobado, pero región
incorrecta o retención activa. Demuestra que la decisión sigue siendo `deny` y conserva:

- el hash de la política aplicada;
- cada razón de rechazo;
- la versión del verificador;
- las garantías y límites declarados.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] Ninguna clave se libera antes de verificar attestation y política.
- [ ] La conclusión no presenta la simulación como ejecución en un TEE real.
- [ ] El threat model incluye host, side channels, salida del modelo y cadena de suministro.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
