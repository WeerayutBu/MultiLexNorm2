import os
import argparse


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, default='mfr')
    parser.add_argument('--path_script', type=str, default='scripts/baseline.py')
    parser.add_argument('--train', type=str, default='data/train')
    parser.add_argument('--pred', type=str, default='data/dev_masked')
    parser.add_argument('--out', type=str, default='output/dev_masked')
    return parser.parse_args()


def list_files(root_dir):
    collect_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if not '.norm' in file: continue
            collect_files.append(os.path.join(dirpath, file))
    return collect_files


def main(args):
    method = args.method
    path_script = args.path_script
    
    ## Strictly check the number of files in train and pred directories
    # assert len(list_files(args.pred))   \
    #     == len(list_files(args.path_data_train)), \
    #     ValueError('Number of files in train and dev directories must be equal')
        
    # Iterative to all prediction files
    for pred_path in list_files(args.pred):
        filename = os.path.basename(pred_path)
        # Link to the train file
        train_path = pred_path.replace(args.pred, args.train)
        train_path = train_path.replace(filename, 'train.norm')
        # Link to the output file
        output_path = pred_path.replace(args.pred, args.out + '_' + method) 
        output_path = output_path + '.pred'
        output_path = output_path.replace('.masked', '')
        
        # Construct command
        cmd = f'python {path_script}'
        cmd += f' --method {method}'
        cmd += f' --train {train_path}'
        cmd += f' --dev {pred_path}'
        cmd += f' --out {output_path}'
        cmd += f' > {output_path.replace(".pred", ".score")}'
        
        # Create directory for each language if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Execute the command
        print(f'running: {cmd}')
        os.system(cmd)

if "__main__" == __name__:
    main(args())
