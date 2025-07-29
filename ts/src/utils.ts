import { Readable } from "stream";
import Speaker from "speaker";
import * as readline from "readline/promises";
import { renderFilled } from "oh-my-logo";

export async function renderLogo(): Promise<void> {
  const logo = await renderFilled("LIVE CHAT", {
    palette: ["#F8E9D8", "#FFA6EA", "#45DFF8", "#BB8DEB"],
  });
  console.log(logo);
}

/**
 * Plays raw PCM audio (16-bit LE, mono, 24000Hz) through the system speaker.
 * @param pcmBuffer - A Buffer of raw PCM data (Int16LE, mono, 24000 Hz).
 */
export function outputAudio(pcmBuffer: Buffer): void {
  const speaker = new Speaker({
    channels: 1,
    bitDepth: 16,
    sampleRate: 24000,
  });

  const readable = new Readable();
  readable.push(pcmBuffer);
  readable.push(null); // Signal end of stream
  readable.pipe(speaker);
}

export function decodePCMData(dataLine: string): Buffer {
  // Decode base64 string into a Buffer
  return Buffer.from(dataLine, "base64");
}

export async function consoleInput(): Promise<string> {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const answer = await rl.question("Your message to Gemini: ");
  rl.close();
  return answer;
}
