import { gemini, GEMINI_MODEL } from "@llamaindex/google";
import { outputAudio, decodePCMData, consoleInput, renderLogo } from "./utils";
import { logger } from "./logger";
import pc from "picocolors";

export async function main(): Promise<number> {
  // Server-side: Generate ephemeral key
  const serverLlm = gemini({
    model: GEMINI_MODEL.GEMINI_2_0_FLASH_LIVE,
    httpOptions: { apiVersion: "v1alpha" },
  });
  const ephemeralKey = await serverLlm.live.getEphemeralKey();

  // Client-side: Use ephemeral key for Live API
  const llm = gemini({
    apiKey: ephemeralKey,
    model: GEMINI_MODEL.GEMINI_2_0_FLASH_LIVE,
    voiceName: "Zephyr",
    httpOptions: { apiVersion: "v1alpha" },
  });

  const session = await llm.live.connect();
  await renderLogo();
  logger.log(
    `Welcome to ${pc.bold(pc.cyan("✨Live Chat✨"))}, our demo for ${pc.bold(
      pc.magenta("Gemini Live🎙️"),
    )} and ${pc.bold(
      pc.magenta("LlamaIndexTS🦙"),
    )}.\nWrite messages to Gemini Live and wait for its answer in the chat below.\nIf you wish to exit, just type ${pc.bold(
      pc.gray("quit"),
    )}.\n`,
  );
  while (true) {
    const audioBuffers: Buffer[] = [];
    const userInput = await consoleInput();
    if (userInput == "quit") {
      break;
    }
    session.sendMessage({
      role: "user",
      content: userInput,
    });
    for await (const event of session.streamEvents()) {
      if (event.type == "audio") {
        audioBuffers.push(decodePCMData(event.data));
      } else if (event.type == "text") {
        logger.log(pc.bold(pc.magenta("Gemini:")), event.text);
      } else if (event.type == "turnComplete") {
        break;
      }
    }
    outputAudio(Buffer.concat(audioBuffers));
  }
  return 0;
}

main().catch(console.error);
